import {
  ACHIEVEMENT_METRICS,
  ACHIEVEMENT_TIERS,
  LEVELS,
  TASK_LABELS,
  formatPoints,
  getAchievementProgress,
  getLevelProgress,
  getNewAchievementUnlocks,
  rankLeaderboard,
} from "./gamification-core.mjs";

const state = {
  points: 1020,
  onboardingCompleted: true,
  promptsSubmitted: 428,
  tasksCompleted: 156,
  crmContacts: 1284,
  emailOpenRate: 42,
  activeDays: 41,
  activeClients: 22,
  taskCounts: {
    offer: 9,
    cma: 19,
    follow_up: 93,
    showing: 16,
    appointment: 14,
    crm_contact: 1284,
    listing_presentation: 6,
    listing_sent: 74,
    market_report: 11,
    newsletter: 8,
    social_post: 37,
    dm_sent: 86,
    deal_analysis: 18,
  },
  gci: [
    { year: 2026, amount: 186400, source: "manual", note: "YTD · entered by you" },
    { year: 2025, amount: 214300, source: "email_scan", note: "Confirmed from email scan" },
    { year: 2024, amount: 189000, source: "manual", note: "Entered by you" },
  ],
  partner: null,
  coachReport: null,
};

// Eight-week trend per metric. Production reads user_kpi_daily rollups;
// the prototype hand-pins believable values consistent with the lifetime totals.
const weeklySeries = {
  promptsSubmitted: [31, 28, 37, 34, 41, 39, 47, 57],
  tasksCompleted: [11, 12, 15, 13, 18, 17, 21, 24],
  cma: [1, 0, 2, 1, 1, 2, 2, 3],
  showing: [1, 1, 2, 0, 2, 1, 2, 2],
  offer: [0, 1, 0, 1, 1, 0, 1, 1],
  listing_presentation: [0, 0, 1, 0, 1, 0, 0, 1],
  listing_sent: [4, 5, 6, 5, 7, 6, 8, 9],
  market_report: [1, 0, 1, 1, 1, 1, 2, 1],
  follow_up: [5, 7, 7, 8, 10, 11, 12, 14],
  appointment: [1, 1, 2, 1, 2, 1, 2, 3],
  newsletter: [0, 1, 1, 0, 1, 1, 1, 1],
  emailOpenRate: [38, 39, 41, 40, 42, 41, 43, 42],
  social_post: [2, 3, 3, 4, 3, 4, 5, 5],
  dm_sent: [6, 7, 8, 9, 10, 11, 12, 13],
  crmContacts: [30, 42, 38, 51, 44, 58, 63, 71],
};

const KPI_CATALOG = [
  { key: "promptsSubmitted", label: "Prompts submitted", note: "Accepted by Homies", icon: "prompt", stage: "usage", achievement: "prompts_submitted", value: () => state.promptsSubmitted },
  { key: "tasksCompleted", label: "AI tasks completed", note: "Verified successful runs", icon: "tasks", stage: "usage", achievement: "tasks_completed", value: () => state.tasksCompleted },
  { key: "emailOpenRate", label: "Email open rate", note: "30-day weighted average", icon: "open_rate", stage: "usage", value: () => state.emailOpenRate, suffix: "%", gauge: true },
  { key: "follow_up", label: "Follow-ups completed", note: "Sent or logged", icon: "follow_up", stage: "pipeline", achievement: "follow_up", value: () => state.taskCounts.follow_up },
  { key: "dm_sent", label: "DMs sent", note: "Sent through linked channels", icon: "dm", stage: "pipeline", achievement: "dm_sent", value: () => state.taskCounts.dm_sent },
  { key: "social_post", label: "Social posts made", note: "Published through connected accounts", icon: "social", stage: "pipeline", achievement: "social_post", value: () => state.taskCounts.social_post },
  { key: "newsletter", label: "Newsletters sent", note: "Campaigns delivered", icon: "mail", stage: "pipeline", achievement: "newsletter", value: () => state.taskCounts.newsletter },
  { key: "crmContacts", label: "Contacts activated", note: "Private · not Impact Points", icon: "contacts", stage: "pipeline", achievement: "crm_contact", value: () => state.crmContacts },
  { key: "cma", label: "CMAs & home valuations", note: "Combined valuation workflow", icon: "cma", stage: "clients", achievement: "cma", value: () => state.taskCounts.cma },
  { key: "showing", label: "Showings booked", note: "Confirmed, not requested", icon: "showing", stage: "clients", achievement: "showing", value: () => state.taskCounts.showing },
  { key: "appointment", label: "Appointments booked", note: "Confirmed calendar events", icon: "appointment", stage: "clients", achievement: "appointment", value: () => state.taskCounts.appointment },
  { key: "listing_sent", label: "Listings sent to buyers", note: "Buyer matches delivered", icon: "send", stage: "clients", achievement: "listing_sent", value: () => state.taskCounts.listing_sent },
  { key: "market_report", label: "Market reports sent", note: "Completed and delivered", icon: "report", stage: "clients", achievement: "market_report", value: () => state.taskCounts.market_report },
  { key: "offer", label: "Offers completed", note: "Saved, exported or sent", icon: "offer", stage: "deals", achievement: "offer", value: () => state.taskCounts.offer },
  { key: "listing_presentation", label: "Listing presentations", note: "Completed pitch decks", icon: "presentation", stage: "deals", achievement: "listing_presentation", value: () => state.taskCounts.listing_presentation },
];

const SCOREBOARD_STAGES = [
  { key: "usage", title: "Working with Homies", note: "Prompts in, verified work out" },
  { key: "pipeline", title: "Pipeline building", note: "Prospecting, nurture and audience" },
  { key: "clients", title: "Active client work", note: "Valuations, tours and reports" },
  { key: "deals", title: "Deals", note: "Offers and pitches — the work that pays" },
];

const FOLLOWUP_BENCHMARK = 8;

let visibleKpis;
try {
  const saved = JSON.parse(localStorage.getItem("homies-visible-kpis") ?? "null");
  visibleKpis = Array.isArray(saved) ? saved.filter((key) => KPI_CATALOG.some((item) => item.key === key)) : KPI_CATALOG.map((item) => item.key);
} catch {
  visibleKpis = KPI_CATALOG.map((item) => item.key);
}

const series = [
  { label: "Apr 20", prompts: 18, tasks: 6, cma: 1, offer: 0, follow_up: 3, appointment: 1 },
  { label: "Apr 27", prompts: 24, tasks: 8, cma: 0, offer: 1, follow_up: 5, appointment: 1 },
  { label: "May 4", prompts: 21, tasks: 10, cma: 2, offer: 0, follow_up: 5, appointment: 2 },
  { label: "May 11", prompts: 31, tasks: 12, cma: 1, offer: 1, follow_up: 7, appointment: 1 },
  { label: "May 18", prompts: 28, tasks: 11, cma: 1, offer: 0, follow_up: 7, appointment: 2 },
  { label: "May 25", prompts: 37, tasks: 15, cma: 2, offer: 1, follow_up: 8, appointment: 1 },
  { label: "Jun 1", prompts: 34, tasks: 13, cma: 1, offer: 0, follow_up: 8, appointment: 1 },
  { label: "Jun 8", prompts: 41, tasks: 18, cma: 2, offer: 1, follow_up: 10, appointment: 2 },
  { label: "Jun 15", prompts: 39, tasks: 17, cma: 1, offer: 0, follow_up: 11, appointment: 1 },
  { label: "Jun 22", prompts: 47, tasks: 21, cma: 2, offer: 1, follow_up: 12, appointment: 2 },
  { label: "Jun 29", prompts: 51, tasks: 23, cma: 2, offer: 0, follow_up: 14, appointment: 2 },
  { label: "Jul 6", prompts: 57, tasks: 24, cma: 3, offer: 1, follow_up: 14, appointment: 3 },
];

const chartSeries = {
  prompts: { label: "Prompts", color: "#d85a30", active: true },
  tasks: { label: "All tasks", color: "#1d9e75", active: true },
  cma: { label: "CMAs", color: "#8468c9", active: true },
  offer: { label: "Offers", color: "#c7872f", active: false },
  follow_up: { label: "Follow-ups", color: "#4f86c6", active: false },
  appointment: { label: "Appointments", color: "#b55e86", active: false },
};

const leaderboardEntries = [
  { publicId: "maya", displayName: "Maya R.", level: 7, points: 612, promptsSubmitted: 174, tasksCompleted: 88, taskCounts: { follow_up: 138, showing: 42, appointment: 27, cma: 100, offer: 52, listing_presentation: 24, listing_sent: 190, market_report: 31, newsletter: 18, social_post: 74, dm_sent: 212, crm_contact: 410 }, movement: 1, color: "#795dbe", badge: 100 },
  { publicId: "alex", displayName: "Alex P.", level: 6, points: 540, promptsSubmitted: 190, tasksCompleted: 70, taskCounts: { follow_up: 121, showing: 39, appointment: 24, cma: 106, offer: 61, listing_presentation: 32, listing_sent: 171, market_report: 28, newsletter: 22, social_post: 61, dm_sent: 198, crm_contact: 382 }, movement: 0, color: "#317c65", badge: 50 },
  { publicId: "you", displayName: "Taylor M.", level: 5, points: 418, promptsSubmitted: 138, tasksCompleted: 56, taskCounts: { follow_up: 93, showing: 16, appointment: 14, cma: 19, offer: 9, listing_presentation: 6, listing_sent: 74, market_report: 11, newsletter: 8, social_post: 37, dm_sent: 86, crm_contact: 176 }, movement: 2, color: "#d85a30", badge: 20, isCurrentUser: true },
  { publicId: "priya", displayName: "Priya S.", level: 5, points: 365, promptsSubmitted: 140, tasksCompleted: 45, taskCounts: { follow_up: 88, showing: 34, appointment: 20, cma: 76, offer: 35, listing_presentation: 21, listing_sent: 132, market_report: 25, newsletter: 16, social_post: 95, dm_sent: 144, crm_contact: 260 }, movement: -1, color: "#4f86c6", badge: 20 },
  { publicId: "jordan", displayName: "Jordan K.", level: 4, points: 292, promptsSubmitted: 102, tasksCompleted: 38, taskCounts: { follow_up: 71, showing: 29, appointment: 17, cma: 61, offer: 31, listing_presentation: 18, listing_sent: 118, market_report: 21, newsletter: 12, social_post: 48, dm_sent: 117, crm_contact: 221 }, movement: 1, color: "#b96b87", badge: 10 },
  { publicId: "sam", displayName: "Sam L.", level: 4, points: 271, promptsSubmitted: 116, tasksCompleted: 31, taskCounts: { follow_up: 64, showing: 21, appointment: 19, cma: 55, offer: 23, listing_presentation: 15, listing_sent: 104, market_report: 19, newsletter: 14, social_post: 53, dm_sent: 126, crm_contact: 204 }, movement: -2, color: "#9c763d", badge: 10 },
  { publicId: "nina", displayName: "Nina V.", level: 4, points: 244, promptsSubmitted: 99, tasksCompleted: 29, taskCounts: { follow_up: 52, showing: 27, appointment: 12, cma: 50, offer: 20, listing_presentation: 11, listing_sent: 96, market_report: 17, newsletter: 10, social_post: 44, dm_sent: 99, crm_contact: 193 }, movement: 0, color: "#427998", badge: 20 },
  { publicId: "liam", displayName: "Liam D.", level: 3, points: 198, promptsSubmitted: 83, tasksCompleted: 23, taskCounts: { follow_up: 48, showing: 18, appointment: 11, cma: 40, offer: 17, listing_presentation: 9, listing_sent: 82, market_report: 13, newsletter: 7, social_post: 31, dm_sent: 84, crm_contact: 184 }, movement: 3, color: "#85684e", badge: 10 },
];

const metricLabels = {
  points: "Impact points",
  tasksCompleted: "Tasks completed",
  promptsSubmitted: "Prompts",
  follow_up: "Follow-ups",
  showing: "Showings booked",
  appointment: "Appointments",
  cma: "CMAs & home valuations",
  offer: "Offers",
  listing_presentation: "Listing presentations",
  listing_sent: "Listings sent",
  market_report: "Market reports sent",
  newsletter: "Newsletters sent",
  social_post: "Social posts",
  dm_sent: "DMs sent",
  crm_contact: "Contacts activated",
};

const profileData = {
  maya: { name: "Maya R.", initials: "MR", market: "Toronto", level: "Level 7 · Accelerator", headline: "Turning market data into confident client conversations.", followers: "842", rank: "#2 CMAs", badges: [["cma", 100], ["offer", 50], ["showing", 20]], kpis: [["CMAs", 100], ["Offers", 52], ["Showings", 42]] },
  priya: { name: "Priya S.", initials: "PS", market: "Vancouver", level: "Level 5 · Operator", headline: "Fast, personal follow-up systems for busy buyer agents.", followers: "516", rank: "#3 Social", badges: [["appointment", 20], ["social_post", 50], ["follow_up", 50]], kpis: [["Social posts", 95], ["Appointments", 20], ["Follow-ups", 88]] },
  jordan: { name: "Jordan K.", initials: "JK", market: "Calgary", level: "Level 4 · Builder", headline: "Learning in public and tightening the buyer journey.", followers: "214", rank: "Top 30%", badges: [["follow_up", 10], ["showing", 20], ["cma", 20]], kpis: [["Follow-ups", 71], ["Showings", 29], ["CMAs", 35]] },
  dave: { name: "Dave Carey", initials: "DC", market: "Ottawa", level: "Level 8 · Rainmaker", headline: "AI Realtor workflows, practical scripts, and a better weekly pipeline review.", followers: "1.8k", rank: "#4 Follow-ups", badges: [["follow_up", 250], ["appointment", 100], ["social_post", 100]], kpis: [["Follow-ups", 278], ["Appointments", 117], ["Social posts", 143]], creator: true },
  you: { name: "Taylor M.", initials: "TM", market: "Toronto", level: "Level 5 · Operator", headline: "Building a more consistent pipeline with Homies.", followers: "128", rank: "#3 Team", badges: [["follow_up", 50], ["showing", 10], ["offer", 5]], kpis: [["Follow-ups", 93], ["Showings", 16], ["Offers", 9]] },
};

const partnerOrganizations = {
  golfi: {
    id: "golfi",
    name: "Golfi Team concept",
    productName: "Golfi Team AI",
    initials: "GT",
    type: "Team & brokerage workspace",
    tagline: "A collective accountability layer for agents, team leads and brokerage operators.",
    domain: "ai.golfiteam.example",
    color: "#d85a30",
    memberCount: 126,
    activeRate: 84,
    rank: 2,
    stats: [
      ["Verified work", "1,842", "+18% vs last month"],
      ["On pace", "76%", "96 members at goal pace"],
      ["Needs support", "9", "Private manager queue"],
      ["Partner-attributed MRR", "$18.4k", "Illustrative channel value"],
    ],
    activity: {
      tasks: [92, 108, 114, 121, 118, 137, 144, 151, 163, 170, 184, 196],
      points: [460, 521, 575, 602, 594, 686, 731, 754, 811, 846, 914, 982],
      active: [68, 71, 73, 76, 75, 79, 82, 85, 87, 91, 98, 106],
    },
    funnel: [["Invited", 214, 100], ["Activated", 172, 80], ["Weekly active", 126, 59], ["90-day retained", 118, 55]],
    rankings: {
      per_agent: [
        [1, "Faris Team concept", 118, 16.2, 1], [2, "Golfi Team concept", 126, 15.6, 2], [3, "RE/MAX brokerage demo", 204, 14.9, 0], [4, "Northstar Realty demo", 61, 13.8, -1],
      ],
      total: [
        [1, "RE/MAX brokerage demo", 204, 3040, 1], [2, "Golfi Team concept", 126, 1966, 1], [3, "Faris Team concept", 118, 1912, -1], [4, "Northstar Realty demo", 61, 842, 0],
      ],
    },
    members: [
      { publicId: "you", name: "Taylor M.", initials: "TM", memberships: [["Golfi Team", "team"], ["Ferry Coaching", "coach"]], group: "Listing Growth Pod", week: "38 / 45 pts", level: 5, status: "on_track", note: "On track" },
      { publicId: "maya", name: "Maya R.", initials: "MR", memberships: [["Golfi Team", "team"]], group: "Hamilton Office", week: "51 / 50 pts", level: 7, status: "on_track", note: "Goal reached" },
      { publicId: "jordan", name: "Jordan K.", initials: "JK", memberships: [["Golfi Team", "team"], ["Q3 Momentum", "coach"]], group: "Buyer Conversion", week: "22 / 40 pts", level: 4, status: "support", note: "Needs support" },
      { publicId: "alex", name: "Alex P.", initials: "AP", memberships: [["Golfi Team", "team"]], group: "Niagara Office", week: "44 / 45 pts", level: 6, status: "on_track", note: "On track" },
      { publicId: "pending-1", name: "Morgan C.", initials: "MC", memberships: [["Golfi Team", "team"]], group: "Unassigned", week: "—", level: 1, status: "invited", note: "Invite pending" },
    ],
    cohorts: [
      { name: "Listing Growth Pod", kind: "Team pod", members: 18, onPace: 83, goal: "10 listing presentations / month", lead: "Maya R." },
      { name: "Buyer Conversion", kind: "Accountability group", members: 24, onPace: 71, goal: "12 confirmed appointments / week", lead: "Alex P." },
      { name: "Hamilton Office", kind: "Office", members: 42, onPace: 79, goal: "500 verified tasks / quarter", lead: "Jordan K." },
    ],
    tree: [["Golfi Team concept", "Organization", 126], ["Hamilton Office", "Office", 42], ["Niagara Office", "Office", 31], ["Listing Growth Pod", "Pod", 18]],
  },
  ferry: {
    id: "ferry",
    name: "Ferry Coaching concept",
    productName: "Ferry Coaching AI",
    initials: "TF",
    type: "Coaching organization",
    tagline: "Programs, cohorts and measurable execution for a distributed coaching community.",
    domain: "ai.ferrycoaching.example",
    color: "#4169a8",
    memberCount: 842,
    activeRate: 72,
    rank: 4,
    stats: [
      ["Verified work", "7,240", "+12% vs last month"],
      ["On pace", "71%", "598 members at goal pace"],
      ["Needs coach check-in", "63", "Private assigned queue"],
      ["Partner-attributed MRR", "$94.2k", "Illustrative channel value"],
    ],
    activity: {
      tasks: [410, 438, 472, 505, 493, 531, 558, 590, 606, 644, 681, 724],
      points: [2048, 2190, 2362, 2521, 2468, 2660, 2795, 2950, 3042, 3221, 3404, 3620],
      active: [402, 431, 456, 472, 468, 491, 513, 538, 551, 574, 588, 604],
    },
    funnel: [["Invited", 1280, 100], ["Activated", 1018, 80], ["Weekly active", 604, 47], ["90-day retained", 552, 43]],
    rankings: {
      per_agent: [
        [1, "Momentum Coaching demo", 318, 12.8, 1], [2, "Relationship Academy demo", 244, 12.4, 0], [3, "Pipeline Lab demo", 176, 12.1, 2], [4, "Ferry Coaching concept", 604, 12.0, -1],
      ],
      total: [
        [1, "Ferry Coaching concept", 604, 7240, 0], [2, "Momentum Coaching demo", 318, 4070, 1], [3, "Relationship Academy demo", 244, 3026, -1], [4, "Pipeline Lab demo", 176, 2131, 0],
      ],
    },
    members: [
      { publicId: "you", name: "Taylor M.", initials: "TM", memberships: [["Ferry Coaching", "coach"], ["Golfi Team", "team"]], group: "Q3 Momentum", week: "38 / 40 pts", level: 5, status: "on_track", note: "On track" },
      { publicId: "priya", name: "Priya S.", initials: "PS", memberships: [["Ferry Coaching", "coach"]], group: "Creator Accelerator", week: "46 / 45 pts", level: 5, status: "on_track", note: "Goal reached" },
      { publicId: "dave", name: "Dave Carey", initials: "DC", memberships: [["Ferry Coaching", "coach"], ["Creator Council", "coach"]], group: "AI Influencer Lab", week: "61 / 55 pts", level: 8, status: "on_track", note: "Goal reached" },
      { publicId: "sam", name: "Sam L.", initials: "SL", memberships: [["Ferry Coaching", "coach"]], group: "Q3 Momentum", week: "18 / 40 pts", level: 4, status: "support", note: "Needs check-in" },
      { publicId: "pending-2", name: "Avery N.", initials: "AN", memberships: [["Ferry Coaching", "coach"]], group: "New member", week: "—", level: 1, status: "invited", note: "Invite pending" },
    ],
    cohorts: [
      { name: "Q3 Momentum", kind: "90-day cohort", members: 84, onPace: 76, goal: "40 Impact points / week", lead: "Coach Serena" },
      { name: "Creator Accelerator", kind: "Program", members: 126, onPace: 69, goal: "3 published assets / week", lead: "Coach Marcus" },
      { name: "AI Influencer Lab", kind: "Advanced cohort", members: 38, onPace: 87, goal: "10 shared workflows / month", lead: "Dave Carey" },
    ],
    tree: [["Ferry Coaching concept", "Organization", 842], ["Core Program", "Program", 412], ["Q3 Momentum", "Cohort", 84], ["Creator Accelerator", "Cohort", 126]],
  },
};

let currentPartnerOrgId = "golfi";
let currentPartnerView = "overview";

const tierIndexFor = (milestone) => Math.max(0, ACHIEVEMENT_TIERS.findIndex((tier) => tier.milestone === milestone));

function achievementFor(metric, milestone) {
  return getAchievementProgress(metric, milestone).catalog.find((item) => item.milestone === milestone);
}

function achievementCounts() {
  return { ...state.taskCounts, prompts_submitted: state.promptsSubmitted, tasks_completed: state.tasksCompleted };
}

function badgeMarkup(achievement, { compact = false } = {}) {
  const tierIndex = tierIndexFor(achievement.milestone);
  const icon = ACHIEVEMENT_ICONS[achievement.metric] ?? iconPaths.tasks;
  return `<span class="badge-mark tier-${tierIndex} ${compact ? "compact" : ""}" style="--badge-color:${achievement.color}" title="${achievement.title} · ${achievement.milestone} ${achievement.metricLabel}"><svg viewBox="0 0 24 24" aria-hidden="true">${icon}</svg><span>${formatPoints(achievement.milestone)}</span><small>${compact ? "" : achievement.metricLabel.replace(" booked", "")}</small></span>`;
}

const iconPaths = {
  prompt: '<path d="M5 5.5A2.5 2.5 0 0 1 7.5 3h9A2.5 2.5 0 0 1 19 5.5v7a2.5 2.5 0 0 1-2.5 2.5H10l-5 4v-4.5A2.5 2.5 0 0 1 4 12.5Z"/><path d="M12 6.2v5.2M9.4 8.8h5.2"/>',
  tasks: '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4a3 3 0 0 1 6 0"/><path d="m8.5 13.5 2.4 2.4 4.6-5"/>',
  contacts: '<circle cx="9" cy="8.5" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M15.5 5.4a3.5 3.5 0 0 1 0 6.2M17 13.6a6.5 6.5 0 0 1 4.5 6.4"/>',
  follow_up: '<path d="M20 11a8.1 8.1 0 0 0-15.5-2M4 4v5h5"/><path d="M4 13a8.1 8.1 0 0 0 15.5 2M20 20v-5h-5"/><circle cx="12" cy="12" r="1.6"/>',
  appointment: '<path d="M6 2.5v3m12-3v3M3.5 9h17M5 4.5h14A1.5 1.5 0 0 1 20.5 6v14.5h-17V6A1.5 1.5 0 0 1 5 4.5Z"/><path d="m8.5 14 2.4 2.4 4.6-5"/>',
  cma: '<path d="m3 11.5 9-7.5 9 7.5"/><path d="M5.5 10v10.5h13V10"/><path d="m8.5 16.5 2.3-2.4 1.8 1.8 2.9-3.2"/>',
  home: '<path d="m3 11 9-8 9 8v10h-6v-6H9v6H3Z"/>',
  offer: '<path d="M6 2h9l4 4v16H6Z"/><path d="M14 2v5h5"/><path d="M9 12.5h6"/><path d="M9 16.5c1-.9 1.7.9 2.7 0s1.6.9 2.6 0"/>',
  showing: '<circle cx="8" cy="8.5" r="4.5"/><path d="m11.3 11.8 8.2 8.2"/><path d="m15.6 16.1 2-2M18 18.5l2-2"/>',
  presentation: '<path d="M3.5 4.5h17V15h-17Z"/><path d="M12 2.5v2m0 10.5V17m-4.5 4.5L12 17l4.5 4.5"/><path d="M7 12V9.5m3.3 2.5V7.5m3.4 4.5V9m3.3 3V8"/>',
  send: '<path d="m3.5 11.5 17-7.5-5 16.5-4-6.5Z"/><path d="M11.5 14 20.5 4"/>',
  report: '<path d="M5.5 3h13v18h-13Z"/><path d="M9 17v-4.5m3 4.5V9.5m3 7.5v-3"/><path d="M9 6.5h6"/>',
  mail: '<path d="M3.5 6.5h17v12h-17Z"/><path d="m3.5 8 8.5 5.5L20.5 8"/>',
  open_rate: '<path d="M2 12s4-6 10-6 10 6 10 6-4 6-10 6S2 12 2 12Z"/><circle cx="12" cy="12" r="2.5"/>',
  social: '<path d="M4 10.5v3.5h2.8l4.7 4V6.5l-4.7 4Z"/><path d="M15 9.2a4.2 4.2 0 0 1 0 6M17.7 6.6a8 8 0 0 1 0 11.2"/>',
  dm: '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8a2.5 2.5 0 0 1-2.5 2.5H10l-5 4v-4.5A2.5 2.5 0 0 1 4 13.5Z"/><path d="m8.3 11.3 7.4-2.9-3.2 4.9-1.5-1.6Z"/>',
  touches: '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.8"/><circle cx="12" cy="12" r="1.4"/>',
  gci: '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v10M14.8 9.2a3.2 3.2 0 0 0-2.8-1.2c-1.7 0-2.8.9-2.8 2.1 0 2.8 5.6 1.4 5.6 4.1 0 1.2-1.1 2.1-2.8 2.1a3.4 3.4 0 0 1-2.9-1.3"/>',
  lock: '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
};

// One purpose-drawn icon per achievement quest line. Badges render these at
// every size (feed posts, pins, tracks, share cards) via badgeMarkup.
const ACHIEVEMENT_ICONS = {
  prompts_submitted: iconPaths.prompt,
  tasks_completed: iconPaths.tasks,
  offer: iconPaths.offer,
  cma: iconPaths.cma,
  follow_up: iconPaths.follow_up,
  showing: iconPaths.showing,
  appointment: iconPaths.appointment,
  crm_contact: iconPaths.contacts,
  listing_presentation: iconPaths.presentation,
  listing_sent: iconPaths.send,
  market_report: iconPaths.report,
  newsletter: iconPaths.mail,
  social_post: iconPaths.social,
  dm_sent: iconPaths.dm,
};

function sparklineMarkup(values, { gauge = false } = {}) {
  const width = 104;
  const height = 30;
  const max = Math.max(...values, 1);
  const min = gauge ? Math.min(...values) : 0;
  const span = Math.max(1, max - min);
  const x = (index) => 3 + (index / (values.length - 1)) * (width - 6);
  const y = (value) => 3 + (1 - (value - min) / span) * (height - 8);
  const points = values.map((value, index) => `${x(index).toFixed(1)},${y(value).toFixed(1)}`).join(" ");
  const area = `M${x(0).toFixed(1)},${height - 2} L${points.replace(/ /g, " L")} L${x(values.length - 1).toFixed(1)},${height - 2} Z`;
  return `<svg viewBox="0 0 ${width} ${height}" aria-hidden="true" focusable="false"><path class="spark-area" d="${area}"/><polyline class="spark-line" points="${points}"/><circle class="spark-dot" cx="${x(values.length - 1).toFixed(1)}" cy="${y(values.at(-1)).toFixed(1)}" r="2.4"/></svg>`;
}

function weekDeltaMarkup(values, { gauge = false } = {}) {
  const current = values.at(-1);
  const previous = values.at(-2) ?? 0;
  if (gauge) {
    const diff = current - previous;
    const direction = diff > 0 ? "up" : diff < 0 ? "down" : "flat";
    return `<small class="delta ${direction}">${diff > 0 ? "↑" : diff < 0 ? "↓" : "→"} ${Math.abs(diff)} pt${Math.abs(diff) === 1 ? "" : "s"}</small>`;
  }
  if (previous === 0) return `<small class="delta ${current > 0 ? "up" : "flat"}">${current > 0 ? "↑ new pace" : "→ quiet week"}</small>`;
  const percent = Math.round(((current - previous) / previous) * 100);
  const direction = percent > 0 ? "up" : percent < 0 ? "down" : "flat";
  return `<small class="delta ${direction}">${percent > 0 ? "↑" : percent < 0 ? "↓" : "→"} ${Math.abs(percent)}% vs last wk</small>`;
}

function questChipMarkup(kpi) {
  if (!kpi.achievement) return '<small class="quest-note">Benchmark only · never scored</small>';
  const progress = getAchievementProgress(kpi.achievement, achievementCounts()[kpi.achievement] ?? Math.round(kpi.value()));
  if (!progress.next) return '<small class="quest-note">Legend complete</small>';
  return `<small class="quest-note">${formatPoints(progress.remaining)} to ${progress.next.title}</small><div class="mini-meter" aria-hidden="true"><span style="width:${progress.progressPercent}%;--track-color:${progress.next.color}"></span></div>`;
}

function scoreRowMarkup(kpi) {
  const values = weeklySeries[kpi.key] ?? [0, 0, 0, 0, 0, 0, 0, 0];
  return `
    <div class="score-row" data-kpi="${kpi.key}">
      <span class="kpi-icon" aria-hidden="true"><svg viewBox="0 0 24 24">${iconPaths[kpi.icon]}</svg></span>
      <div class="score-name"><strong>${kpi.label}</strong><small>${kpi.note}${kpi.gauge ? " · benchmark only" : ""}</small></div>
      <div class="score-spark">${sparklineMarkup(values, { gauge: kpi.gauge })}</div>
      <div class="score-week"><strong>${formatPoints(values.at(-1))}${kpi.suffix ?? ""}</strong>${weekDeltaMarkup(values, { gauge: kpi.gauge })}<small class="score-week-label">this week</small></div>
      <div class="score-life"><strong>${formatPoints(kpi.value())}${kpi.suffix ?? ""}</strong><small>${kpi.gauge ? "30-day avg" : "lifetime"}</small></div>
      <div class="score-quest">${questChipMarkup(kpi)}</div>
      <button class="kpi-remove" data-remove-kpi="${kpi.key}" type="button" aria-label="Remove ${kpi.label} from dashboard">×</button>
    </div>`;
}

function followupTouchesRowMarkup() {
  const touches = state.taskCounts.follow_up / state.activeClients;
  const onPace = touches >= FOLLOWUP_BENCHMARK;
  return `
    <div class="score-row derived-row" data-kpi="avg_touches">
      <span class="kpi-icon" aria-hidden="true"><svg viewBox="0 0 24 24">${iconPaths.touches}</svg></span>
      <div class="score-name"><strong>Avg follow-up attempts per client</strong><small>${formatPoints(state.taskCounts.follow_up)} follow-ups across ${state.activeClients} active clients</small></div>
      <div class="score-spark"><span class="benchmark-pill ${onPace ? "good" : ""}">Top agents: ${FOLLOWUP_BENCHMARK}+ touches</span></div>
      <div class="score-week score-week-wide"><strong>${touches.toFixed(1)}×</strong><small class="delta ${onPace ? "up" : "flat"}">${onPace ? "At top-agent pace" : `${(FOLLOWUP_BENCHMARK - touches).toFixed(1)} below top agents`}</small></div>
      <div class="score-quest"><small class="quest-note">Most deals close after 5+ touches. Ask Homies to queue the next round.</small></div>
    </div>`;
}

function renderScoreboard() {
  const container = document.querySelector("#scoreboard");
  container.innerHTML = SCOREBOARD_STAGES.map((stage) => {
    const rows = KPI_CATALOG.filter((kpi) => kpi.stage === stage.key && visibleKpis.includes(kpi.key));
    const derived = stage.key === "pipeline" ? followupTouchesRowMarkup() : "";
    if (!rows.length && !derived) return "";
    return `
      <article class="score-group card" data-stage="${stage.key}">
        <header class="score-group-head"><div><h3>${stage.title}</h3><span>${stage.note}</span></div></header>
        <div class="score-rows">${rows.map(scoreRowMarkup).join("")}${derived}</div>
      </article>`;
  }).join("");
  renderMetricPicker();
}

function formatMoney(amount) {
  return `$${new Intl.NumberFormat("en-CA").format(Math.round(amount))}`;
}

function renderGci() {
  const sorted = [...state.gci].sort((a, b) => b.year - a.year);
  const currentYear = sorted.find((record) => record.year === 2026);
  document.querySelector("#gci-current").textContent = currentYear ? formatMoney(currentYear.amount) : "—";
  document.querySelector("#gci-years").innerHTML = sorted.map((record) => `
    <span class="gci-year-chip ${record.source}">
      <strong>${record.year}</strong> ${formatMoney(record.amount)}
      <small>${record.source === "email_scan" ? "✓ email scan" : "manual"}</small>
    </span>`).join("");
}

function saveVisibleKpis() {
  localStorage.setItem("homies-visible-kpis", JSON.stringify(visibleKpis));
}

function renderMetricPicker() {
  const available = KPI_CATALOG.filter((item) => !visibleKpis.includes(item.key));
  document.querySelector("#metric-picker").innerHTML = available.length
    ? available.map((item) => `<button data-add-kpi="${item.key}" type="button"><span class="kpi-icon" aria-hidden="true"><svg viewBox="0 0 24 24">${iconPaths[item.icon]}</svg></span><span><strong>${item.label}</strong><small>${item.note}</small></span><b>+</b></button>`).join("")
    : '<p>All 15 metrics are on your dashboard.<br>Hover a card and press × to remove it.</p>';
}

function renderAchievements() {
  const metrics = Object.keys(ACHIEVEMENT_METRICS);
  const counts = achievementCounts();
  const progressByMetric = metrics.map((metric) => getAchievementProgress(metric, counts[metric] ?? 0));
  const earnedCount = progressByMetric.reduce((sum, item) => sum + item.earned.length, 0);
  document.querySelector("#achievement-earned-count").textContent = earnedCount;

  const closest = progressByMetric
    .filter((item) => item.next)
    .sort((a, b) => a.remaining - b.remaining || b.progressPercent - a.progressPercent)[0];
  const next = closest.next;
  document.querySelector("#next-achievement").innerHTML = `
    <div class="quest-glow" aria-hidden="true"></div>
    ${badgeMarkup(next)}
    <div class="achievement-hero-copy">
      <p class="eyebrow">Closest achievement · ${next.tier}</p>
      <h2>${next.title}</h2>
      <p><strong>${closest.remaining === 1 ? "One more" : `${closest.remaining} more`}</strong> ${next.metricLabel.toLowerCase()} to unlock ${next.rarity} status.</p>
      <div class="quest-progress-label"><span>${formatPoints(closest.count)} / ${formatPoints(next.milestone)}</span><span>${closest.progressPercent}%</span></div>
      <div class="quest-progress" role="progressbar" aria-label="${closest.progressPercent} percent to ${next.title}" aria-valuemin="${closest.current?.milestone ?? 0}" aria-valuemax="${next.milestone}" aria-valuenow="${closest.count}"><span style="width:${closest.progressPercent}%"></span></div>
    </div>
    <a class="button primary" href="#dashboard">Continue this quest</a>`;

  const pins = [["follow_up", 50], ["showing", 10], ["offer", 5]].map(([metric, milestone]) => achievementFor(metric, milestone));
  document.querySelector("#pinned-badges").innerHTML = pins.map((achievement, index) => `
    <article class="pinned-badge-card">
      <span class="pin-number">Slot ${index + 1}</span>${badgeMarkup(achievement)}
      <div><p class="eyebrow">${achievement.tier}</p><h3>${achievement.title}</h3><span>${formatPoints(achievement.milestone)} ${achievement.metricLabel.toLowerCase()}</span></div>
      <button class="icon-share js-share-win" data-metric="${achievement.metric}" data-milestone="${achievement.milestone}" type="button" aria-label="Share ${achievement.title}">↗</button>
    </article>`).join("");

  document.querySelector("#achievement-tracks").innerHTML = progressByMetric.map((progress) => {
    const display = progress.current ?? progress.next;
    const tierIndex = tierIndexFor(display.milestone);
    const nextCopy = progress.next ? `${progress.remaining} to ${progress.next.title}` : "Legend status complete";
    return `<article class="achievement-track">
      <header>${badgeMarkup(display, { compact: true })}<div><h3>${progress.metricLabel}</h3><span>${formatPoints(progress.count)} complete · ${nextCopy}</span></div><strong>${progress.next ? `${progress.progressPercent}%` : "MAX"}</strong></header>
      <div class="track-meter"><span style="width:${progress.progressPercent}%;--track-color:${ACHIEVEMENT_TIERS[tierIndex].color}"></span></div>
      <div class="milestone-row" aria-label="${progress.metricLabel} milestones">
        ${progress.catalog.map((achievement, index) => `<span class="milestone-dot ${progress.count >= achievement.milestone ? "earned" : ""} tier-${index}" title="${achievement.title}: ${achievement.milestone}">${achievement.milestone}</span>`).join("")}
      </div>
      <footer><span>${progress.current ? `${progress.current.title} earned` : "First badge waiting"}</span>${progress.current ? `<button class="text-button js-share-win" data-metric="${progress.metric}" data-milestone="${progress.current.milestone}" type="button">Share win</button>` : ""}</footer>
    </article>`;
  }).join("");
}

function renderBreakdown() {
  const rows = ["follow_up", "dm_sent", "listing_sent", "social_post", "cma", "showing", "appointment", "offer"];
  const colors = ["#d85a30", "#8468c9", "#4f86c6", "#1d9e75", "#9d68ba", "#c7872f", "#5d967c", "#bd5e49"];
  const max = Math.max(...rows.map((key) => state.taskCounts[key]));
  document.querySelector("#task-breakdown").innerHTML = rows.map((key, index) => `
    <div class="breakdown-row">
      <label>${TASK_LABELS[key]}</label><strong>${formatPoints(state.taskCounts[key])}</strong>
      <div class="breakdown-track" aria-hidden="true"><span style="width:${Math.max(5, (state.taskCounts[key] / max) * 100)}%;--bar-color:${colors[index]}"></span></div>
    </div>
  `).join("");
}

function renderChartLegend() {
  const container = document.querySelector("#chart-legend");
  container.innerHTML = Object.entries(chartSeries).map(([key, value]) => `
    <button class="legend-toggle" type="button" data-series="${key}" aria-pressed="${value.active}" style="--series-color:${value.color}">
      <span class="legend-dot" aria-hidden="true"></span>${value.label}
    </button>
  `).join("");
  container.querySelectorAll("button").forEach((button) => {
    button.addEventListener("click", () => {
      const key = button.dataset.series;
      const activeCount = Object.values(chartSeries).filter((item) => item.active).length;
      if (chartSeries[key].active && activeCount === 1) return;
      chartSeries[key].active = !chartSeries[key].active;
      button.setAttribute("aria-pressed", String(chartSeries[key].active));
      renderChart();
    });
  });
}

function renderChart() {
  const count = Number(document.querySelector("#chart-period").value);
  const data = series.slice(-count);
  const active = Object.entries(chartSeries).filter(([, item]) => item.active);
  const width = 760;
  const height = 260;
  const pad = { top: 16, right: 18, bottom: 35, left: 36 };
  const plotWidth = width - pad.left - pad.right;
  const plotHeight = height - pad.top - pad.bottom;
  const rawMax = Math.max(...data.flatMap((item) => active.map(([key]) => item[key] ?? 0)), 1);
  const yMax = Math.max(10, Math.ceil(rawMax / 10) * 10);
  const x = (index) => pad.left + (data.length === 1 ? 0 : (index / (data.length - 1)) * plotWidth);
  const y = (value) => pad.top + plotHeight - (value / yMax) * plotHeight;
  const line = (key) => data.map((item, index) => `${index === 0 ? "M" : "L"}${x(index).toFixed(2)},${y(item[key] ?? 0).toFixed(2)}`).join(" ");
  const promptArea = chartSeries.prompts.active
    ? `<path class="chart-area" d="${line("prompts")} L${x(data.length - 1)},${pad.top + plotHeight} L${x(0)},${pad.top + plotHeight} Z"/>`
    : "";
  const grid = [0, .25, .5, .75, 1].map((ratio) => {
    const value = Math.round(yMax * (1 - ratio));
    const yPos = pad.top + plotHeight * ratio;
    return `<line class="chart-grid-line" x1="${pad.left}" y1="${yPos}" x2="${width - pad.right}" y2="${yPos}"/><text class="chart-axis-label" x="${pad.left - 8}" y="${yPos + 3}" text-anchor="end">${value}</text>`;
  }).join("");
  const xLabels = data.map((item, index) => {
    if (data.length > 8 && index % 2 === 1 && index !== data.length - 1) return "";
    return `<text class="chart-axis-label" x="${x(index)}" y="${height - 10}" text-anchor="middle">${item.label}</text>`;
  }).join("");
  const lines = active.map(([key, item]) => `
    <path class="chart-line" style="--series-color:${item.color}" d="${line(key)}"/>
    ${data.map((point, index) => `<circle class="chart-point" style="--series-color:${item.color}" cx="${x(index)}" cy="${y(point[key] ?? 0)}" r="2.7"><title>${item.label}, ${point.label}: ${point[key] ?? 0}</title></circle>`).join("")}
  `).join("");

  document.querySelector("#activity-chart").innerHTML = `
    <svg viewBox="0 0 ${width} ${height}" aria-hidden="true" focusable="false">
      <defs><linearGradient id="promptGradient" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#d85a30" stop-opacity=".14"/><stop offset="1" stop-color="#d85a30" stop-opacity="0"/></linearGradient></defs>
      ${grid}${xLabels}${promptArea}${lines}
    </svg>
  `;

  const headings = active.map(([, item]) => `<th scope="col">${item.label}</th>`).join("");
  const rows = data.map((item) => `<tr><th scope="row">${item.label}</th>${active.map(([key]) => `<td>${item[key] ?? 0}</td>`).join("")}</tr>`).join("");
  document.querySelector("#chart-table").innerHTML = `<thead><tr><th scope="col">Week</th>${headings}</tr></thead><tbody>${rows}</tbody>`;
  document.querySelector("#activity-chart").setAttribute("aria-label", `${count}-week activity chart showing ${active.map(([, item]) => item.label).join(", ")}`);
}

function renderHeatmap() {
  const end = new Date("2026-07-12T12:00:00Z");
  const cells = Array.from({ length: 365 }, (_, index) => {
    const date = new Date(end);
    date.setUTCDate(end.getUTCDate() - (364 - index));
    const weekday = date.getUTCDay();
    const wave = (index * 7 + Math.floor(index / 11) * 3) % 13;
    const strength = weekday === 0 ? (wave > 10 ? 1 : 0) : weekday === 6 ? (wave > 8 ? 2 : 0) : wave < 2 ? 0 : wave < 6 ? 1 : wave < 9 ? 2 : wave < 12 ? 3 : 4;
    return `<span data-strength="${strength}" title="${date.toLocaleDateString("en-CA", { month: "short", day: "numeric", year: "numeric", timeZone: "UTC" })}: ${strength === 0 ? "No" : strength} activity ${strength === 1 ? "event" : "events"}"></span>`;
  });
  document.querySelector("#activity-heatmap").innerHTML = cells.join("");
}

function leaderboardForPeriod(period) {
  const factor = period === "week" ? 0.28 : period === "all_time" ? 4.6 : 1;
  return leaderboardEntries.map((entry) => ({
    ...entry,
    points: Math.round(entry.points * factor),
    promptsSubmitted: Math.round(entry.promptsSubmitted * factor),
    tasksCompleted: Math.round(entry.tasksCompleted * factor),
    taskCounts: Object.fromEntries(Object.entries(entry.taskCounts).map(([key, value]) => [key, Math.max(0, Math.round(value * factor))])),
  }));
}

function renderLeaderboard() {
  const metric = document.querySelector("#leaderboard-metric").value;
  const period = document.querySelector("#leaderboard-period").value;
  const ranked = rankLeaderboard(leaderboardForPeriod(period), metric);
  document.querySelector("#metric-column-heading").textContent = metricLabels[metric];
  document.querySelector("#leaderboard-body").innerHTML = ranked.map((entry) => {
    const initials = entry.displayName.split(/\s+/).map((part) => part[0]).join("").slice(0, 2);
    const movement = entry.movement > 0 ? `↑ ${entry.movement}` : entry.movement < 0 ? `↓ ${Math.abs(entry.movement)}` : "—";
    return `
      <tr ${entry.isCurrentUser ? 'aria-current="true"' : ""}>
        <td><span class="rank-number ${entry.rank <= 3 ? "top" : ""}">#${entry.rank}</span></td>
        <td><button class="agent-cell js-open-profile" data-profile="${entry.publicId}" type="button"><span class="mini-avatar" style="--avatar-color:${entry.color}">${initials}</span><span>${entry.displayName}${entry.isCurrentUser ? '<span class="you-pill">You</span>' : ""} <span class="micro-badge tier-${Math.min(8, tierIndexFor(entry.badge))}">${entry.badge}</span></span></button></td>
        <td><span class="table-level"><span>${entry.level}</span>Level ${entry.level}</span></td>
        <td><strong>${formatPoints(entry.value)}</strong></td>
        <td><span class="movement ${entry.movement > 0 ? "up" : ""}">${movement}</span></td>
      </tr>`;
  }).join("");
  const current = ranked.find((entry) => entry.isCurrentUser);
  document.querySelector("#current-rank").textContent = `#${current?.rank ?? "—"}`;
}

function renderLevelLadder() {
  const progress = getLevelProgress({ points: state.points, onboardingCompleted: state.onboardingCompleted });
  document.querySelector("#level-ladder").innerHTML = LEVELS.map((level) => {
    const status = level.level < progress.current.level ? "completed" : level.level === progress.current.level ? "current" : "locked";
    const statusLabel = status === "completed" ? "Complete" : status === "current" ? "You are here" : level.level === 2 ? "Finish setup" : `${formatPoints(level.minimumPoints)} points`;
    return `
      <article class="level-row ${status}" ${status === "current" ? 'aria-current="step"' : ""}>
        <span class="level-row-number">${status === "completed" ? "✓" : level.level}</span>
        <div><h3>Level ${level.level} · ${level.name}</h3><p>${level.requirement}</p></div>
        <span class="level-status">${statusLabel}</span>
      </article>`;
  }).join("");
}

function renderLevelSummary() {
  const progress = getLevelProgress({ points: state.points, onboardingCompleted: state.onboardingCompleted });
  document.querySelectorAll(".level-chip").forEach((chip) => {
    chip.querySelector(".level-chip-number").textContent = `L${progress.current.level}`;
    chip.querySelector(".level-chip-name").textContent = progress.current.name;
    chip.querySelector(".level-chip-track span").style.width = `${progress.progressPercent}%`;
    const nextLabel = progress.next ? `Level ${progress.next.level}` : "the maximum level";
    chip.setAttribute("aria-label", `Level ${progress.current.level}, ${progress.progressPercent} percent to ${nextLabel}. View activity stats.`);
  });

  document.querySelector(".level-medallion span").textContent = progress.current.level;
  document.querySelector("#level-heading").textContent = `Level ${progress.current.level} · ${progress.current.name}`;
  document.querySelector("#hero-points").textContent = formatPoints(state.points);
  document.querySelector("#hero-next-copy").textContent = progress.next ? `${formatPoints(progress.pointsToNext)} to Level ${progress.next.level}` : "Top level reached";
  const bar = document.querySelector(".hero-progress");
  bar.querySelector("span").style.width = `${progress.progressPercent}%`;
  bar.setAttribute("aria-valuemin", progress.current.minimumPoints);
  bar.setAttribute("aria-valuemax", progress.next?.minimumPoints ?? state.points);
  bar.setAttribute("aria-valuenow", state.points);
  bar.setAttribute("aria-label", progress.next ? `${progress.progressPercent} percent to Level ${progress.next.level}` : "Maximum level reached");
  document.querySelector(".level-medallion").style.background = `conic-gradient(var(--brand) 0 ${progress.progressPercent}%, #eadfd8 ${progress.progressPercent}% 100%)`;
  document.querySelector("#war-plan-button").textContent = progress.next ? `⚡ Help me reach Level ${progress.next.level}` : "⚡ Build my personal-best plan";
}

function renderPartnerActivity(org) {
  const metric = document.querySelector("#partner-chart-metric").value;
  const values = org.activity[metric];
  const max = Math.max(...values, 1);
  const labels = { tasks: "verified tasks", points: "Impact points", active: "active members" };
  const chart = document.querySelector("#partner-activity-bars");
  chart.style.setProperty("--chart-color", org.color);
  chart.innerHTML = values.map((value, index) => `<span style="height:${Math.max(8, (value / max) * 100)}%" title="Week ${index + 1}: ${formatPoints(value)} ${labels[metric]}"><i></i></span>`).join("");
  chart.setAttribute("aria-label", `Twelve-week chart of ${labels[metric]} for ${org.name}; latest value ${formatPoints(values.at(-1))}`);
}

function renderPartnerFunnel(org) {
  document.querySelector("#partner-funnel").innerHTML = org.funnel.map(([label, value, percent]) => `<div><header><span>${label}</span><strong>${formatPoints(value)} <small>${percent}%</small></strong></header><div class="funnel-track"><span style="width:${percent}%;--funnel-color:${org.color}"></span></div></div>`).join("");
}

function renderOrganizationRanking(org) {
  const mode = document.querySelector("#organization-ranking-mode").value;
  const rows = org.rankings[mode];
  document.querySelector("#organization-ranking-title").textContent = org.id === "golfi" ? "Team vs. team benchmark" : "Coaching program benchmark";
  document.querySelector("#org-ranking-value-heading").textContent = mode === "per_agent" ? "Tasks / active member" : "Collective tasks";
  document.querySelector("#organization-ranking-body").innerHTML = rows.map(([rank, name, active, value, movement]) => {
    const current = name === org.name;
    const movementCopy = movement > 0 ? `↑ ${movement}` : movement < 0 ? `↓ ${Math.abs(movement)}` : "—";
    return `<tr ${current ? 'aria-current="true"' : ""}><td><strong>#${rank}</strong></td><td><span class="organization-cell"><i style="--org-color:${current ? org.color : "#8b857c"}">${name.split(/\s+/).map((part) => part[0]).join("").slice(0, 2)}</i><span>${name}${current ? '<small>Your organization</small>' : '<small>Public aggregate only</small>'}</span></span></td><td>${formatPoints(active)}</td><td><strong>${mode === "per_agent" ? value.toFixed(1) : formatPoints(value)}</strong></td><td><span class="movement ${movement > 0 ? "up" : ""}">${movementCopy}</span></td></tr>`;
  }).join("");
}

function renderPartnerMembers(org) {
  const filter = document.querySelector("#member-status-filter").value;
  const members = org.members.filter((member) => filter === "all" || member.status === filter);
  document.querySelector("#partner-member-body").innerHTML = members.map((member) => {
    const safeName = escapeHtml(member.name);
    const safeInitials = escapeHtml(member.initials);
    const profileButton = member.publicId.startsWith("pending") ? `<span class="member-avatar muted">${safeInitials}</span>` : `<button class="member-avatar js-open-profile" data-profile="${escapeHtml(member.publicId)}" type="button" aria-label="Open ${safeName} profile">${safeInitials}</button>`;
    return `<tr data-member-status="${member.status}"><td><span class="member-cell">${profileButton}<span><strong>${safeName}</strong><small>${member.status === "invited" ? "Invitation not accepted" : "Portable Homies account"}</small></span></span></td><td><span class="membership-tags">${member.memberships.map(([label, type]) => `<span class="${type}">${escapeHtml(label)}</span>`).join("")}</span></td><td>${escapeHtml(member.group)}</td><td><strong>${escapeHtml(member.week)}</strong></td><td><span class="table-level"><span>${member.level}</span>Level ${member.level}</span></td><td><span class="member-status ${member.status}">${escapeHtml(member.note)}</span></td><td><button class="member-menu" type="button" aria-label="Actions for ${safeName}">•••</button></td></tr>`;
  }).join("") || '<tr><td colspan="7"><div class="empty-members">No members match this filter.</div></td></tr>';
}

function renderPartnerCohorts(org) {
  document.querySelector("#partner-cohort-grid").innerHTML = org.cohorts.map((cohort) => `<article class="partner-cohort-card card"><header><span class="cohort-icon" style="--cohort-color:${org.color}">${cohort.name.slice(0, 1)}</span><div><p class="eyebrow">${cohort.kind}</p><h3>${cohort.name}</h3></div><button type="button" aria-label="More options for ${cohort.name}">•••</button></header><div class="cohort-progress"><span><strong>${cohort.onPace}%</strong> on pace</span><div><i style="width:${cohort.onPace}%;--cohort-color:${org.color}"></i></div></div><dl><div><dt>Members</dt><dd>${cohort.members}</dd></div><div><dt>Lead</dt><dd>${cohort.lead}</dd></div></dl><footer><span>${cohort.goal}</span><button class="text-button" type="button">Open dashboard →</button></footer></article>`).join("");
  document.querySelector("#organization-tree").innerHTML = org.tree.map(([name, type, members], index) => `<div style="--tree-depth:${Math.min(index, 2)}"><i style="--tree-color:${org.color}">${name.split(/\s+/).map((part) => part[0]).join("").slice(0, 2)}</i><span><strong>${name}</strong><small>${type} · ${members} members</small></span></div>`).join("");
}

function renderPartnerBrand(org) {
  const preview = document.querySelector("#white-label-preview");
  preview.style.setProperty("--preview-color", org.color);
  document.querySelector("#white-label-logo").textContent = org.initials;
  document.querySelector("#white-label-name").textContent = org.productName;
  document.querySelector("#white-label-domain").textContent = org.domain;
  document.querySelector("#billing-seats").textContent = formatPoints(org.memberCount);
  document.querySelectorAll("[data-brand-color]").forEach((button) => button.classList.toggle("selected", button.dataset.brandColor === org.color));
  document.querySelector("#invite-preview-logo").textContent = org.initials;
  document.querySelector("#invite-preview-name").textContent = `You’re invited to ${org.productName}`;
}

function renderPartnerHub() {
  const org = partnerOrganizations[currentPartnerOrgId];
  document.querySelector("#partner-org-select").value = currentPartnerOrgId;
  document.querySelector("#partner-hero").style.setProperty("--partner-color", org.color);
  document.querySelector("#partner-logo").textContent = org.initials;
  document.querySelector("#partner-type").textContent = org.type;
  document.querySelector("#partner-name").textContent = org.name;
  document.querySelector("#partner-tagline").textContent = org.tagline;
  document.querySelector("#partner-domain").textContent = org.domain;
  document.querySelector("#partner-member-count").textContent = formatPoints(org.memberCount);
  document.querySelector("#partner-active-rate").textContent = `${org.activeRate}%`;
  document.querySelector("#partner-rank").textContent = `#${org.rank}`;
  document.querySelector("#partner-stat-grid").innerHTML = org.stats.map(([label, value, note], index) => `<article class="partner-stat-card card ${index === 0 ? "accent" : ""}"><small>${label}</small><strong>${value}</strong><span>${note}</span></article>`).join("");
  renderPartnerActivity(org);
  renderPartnerFunnel(org);
  renderOrganizationRanking(org);
  renderPartnerMembers(org);
  renderPartnerCohorts(org);
  renderPartnerBrand(org);
}

function setPartnerView(view) {
  const supported = ["overview", "members", "cohorts", "brand"];
  currentPartnerView = supported.includes(view) ? view : "overview";
  document.querySelectorAll("[data-partner-view]").forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.partnerView === currentPartnerView)));
  document.querySelectorAll("[data-partner-panel]").forEach((panel) => { panel.hidden = panel.dataset.partnerPanel !== currentPartnerView; });
}

function renderAll() {
  renderLevelSummary();
  renderScoreboard();
  renderGci();
  renderAccountability();
  renderAchievements();
  renderBreakdown();
  renderHeatmap();
  renderLevelLadder();
  renderLeaderboard();
  renderPartnerHub();
}

function setActiveTab(name) {
  const supported = ["overview", "achievements", "leaderboard", "community", "partners", "levels"];
  const selected = supported.includes(name) ? name : "overview";
  document.querySelectorAll('[role="tab"]').forEach((tab) => {
    const active = tab.dataset.tab === selected;
    tab.setAttribute("aria-selected", String(active));
    tab.tabIndex = active ? 0 : -1;
  });
  supported.forEach((panel) => {
    document.querySelector(`#${panel}-panel`).hidden = panel !== selected;
  });
  if (selected === "leaderboard") renderLeaderboard();
  if (selected === "partners") renderPartnerHub();
}

function handleRoute() {
  const hash = window.location.hash || "#dashboard";
  const isProgress = hash.startsWith("#progress");
  document.querySelector("#dashboard-view").hidden = isProgress;
  document.querySelector("#progress-view").hidden = !isProgress;
  document.querySelectorAll(".side-nav-link").forEach((link) => {
    const targetProgress = link.getAttribute("href").startsWith("#progress");
    const active = isProgress ? targetProgress && link.getAttribute("href") === hash : !targetProgress && link.getAttribute("href") === "#dashboard";
    link.classList.toggle("active", active);
    if (active) link.setAttribute("aria-current", "page"); else link.removeAttribute("aria-current");
  });
  if (isProgress) {
    setActiveTab(hash.split("/")[1] || "overview");
    document.title = hash.includes("/partners") ? "Partner hub · Homies" : "Your progress · Homies";
  } else {
    document.title = "Homies · Progress prototype";
  }
  window.scrollTo({ top: 0, behavior: "instant" });
}

let toastTimer;
function showToast(message) {
  const toast = document.querySelector("#toast");
  toast.innerHTML = message;
  toast.hidden = false;
  window.clearTimeout(toastTimer);
  toastTimer = window.setTimeout(() => { toast.hidden = true; }, 3500);
}

let currentAchievement = achievementFor("offer", 5);
let pendingPrompt = "";

function ordinal(value) {
  if (value === 1) return "first";
  const remainder = value % 100;
  const suffix = remainder >= 11 && remainder <= 13 ? "th" : value % 10 === 1 ? "st" : value % 10 === 2 ? "nd" : value % 10 === 3 ? "rd" : "th";
  return `${value}${suffix}`;
}

function escapeHtml(value) {
  return String(value).replace(/[&<>'"]/g, (character) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" })[character]);
}

function shareSentence(achievement) {
  const count = ordinal(achievement.milestone);
  const copy = {
    offer: `I just had Homies AI help me write my ${count} offer.`,
    prompts_submitted: `I just submitted my ${count} prompt to Homies AI.`,
    tasks_completed: `I just completed my ${count} AI task with Homies.`,
    cma: `I just completed my ${count} CMA with Homies AI.`,
    follow_up: `I just completed my ${count} follow-up with Homies AI.`,
    showing: `I just booked my ${count} showing with Homies AI.`,
    appointment: `I just booked my ${count} appointment with Homies AI.`,
    crm_contact: `I have now activated ${formatPoints(achievement.milestone)} unique CRM contacts with Homies AI.`,
    listing_presentation: `I just completed my ${count} listing presentation with Homies AI.`,
    listing_sent: `I just sent my ${count} matched listing to a buyer with Homies AI.`,
    market_report: `I just sent my ${count} market report with Homies AI.`,
    newsletter: `I just sent my ${count} newsletter with Homies AI.`,
    social_post: `I just published my ${count} social post with Homies AI.`,
    dm_sent: `I just sent my ${count} DM with Homies AI.`,
  };
  return copy[achievement.metric];
}

function openShareDialog(achievement) {
  currentAchievement = achievement;
  const next = getAchievementProgress(achievement.metric, achievement.milestone).next;
  const caption = `Achievement unlocked: ${achievement.title} 🏆\n${shareSentence(achievement)}\n${achievement.tier} · ${formatPoints(achievement.milestone)} complete${next ? `\nNext quest: ${formatPoints(next.milestone)}` : "\nLegend status earned"}`;
  document.querySelector("#share-caption").value = caption;
  document.querySelector("#share-card").innerHTML = `<div class="share-card-brand">homies <span>beta</span></div><div class="share-card-orbit" aria-hidden="true"></div>${badgeMarkup(achievement)}<div><p>Achievement unlocked</p><h3>${achievement.title}</h3><strong>${formatPoints(achievement.milestone)} ${achievement.metricLabel}</strong></div><footer><span>${achievement.tier}</span><span>@taylormoves</span></footer>`;
  document.querySelector("#share-dialog").showModal();
}

function openProfileDialog(profileId) {
  let profile = profileData[profileId];
  if (!profile) {
    const entry = leaderboardEntries.find((item) => item.publicId === profileId);
    profile = entry ? { name: entry.displayName, initials: entry.displayName.replace(/[^A-Z]/g, "").slice(0, 2), market: "Homies community", level: `Level ${entry.level}`, headline: "Building momentum with verified work through Homies.", followers: "—", rank: "Team member", badges: [["follow_up", entry.badge]], kpis: [["Impact points", entry.points], ["Tasks", entry.tasksCompleted], ["Prompts", entry.promptsSubmitted]] } : profileData.you;
  }
  document.querySelector("#profile-dialog-content").innerHTML = `
    <div class="profile-cover"><span>homies community</span></div>
    <div class="profile-identity"><span class="profile-avatar xlarge">${profile.initials}</span><div><p class="eyebrow">${profile.market}</p><h2 id="profile-dialog-title">${profile.name}${profile.creator ? ' <span class="verified-mark" aria-label="Featured creator">✓</span>' : ""}</h2><span>${profile.level}</span></div><button class="button primary follow-button" type="button">Follow</button></div>
    <p class="profile-headline">${profile.headline}</p>
    <div class="profile-meta"><span><strong>${profile.followers}</strong> followers</span><span><strong>${profile.rank}</strong> visible rank</span><span><strong>${profile.badges.length}</strong> featured badges</span></div>
    <div class="profile-badge-shelf">${profile.badges.map(([metric, milestone]) => { const item = achievementFor(metric, milestone); return `<div>${badgeMarkup(item)}<strong>${item.title}</strong><span>${item.tier}</span></div>`; }).join("")}</div>
    <div class="profile-kpis">${profile.kpis.map(([label, value]) => `<div><strong>${formatPoints(value)}</strong><span>${label}</span></div>`).join("")}</div>
    <div class="profile-feature"><p class="eyebrow">Featured workflow</p><h3>My weekly pipeline reset</h3><p>A practical prompt sequence for turning a messy CRM into five clear next moves.</p><button class="button secondary try-prompt-button" data-prompt="Review my active pipeline for this week. Group opportunities by urgency, identify the five clearest next actions, and draft concise follow-ups for each. Ask me before using any contact data." type="button">Try this workflow</button></div>`;
  document.querySelector("#profile-dialog").showModal();
}

function usePromptTemplate(template, mode = "replace") {
  const input = document.querySelector("#prompt-input");
  input.value = mode === "append" && input.value.trim() ? `${input.value.trim()}\n\n${template}` : template;
  window.location.hash = "#dashboard";
  window.setTimeout(() => { input.focus(); input.setSelectionRange(input.value.length, input.value.length); }, 50);
  showToast("<strong>Prompt draft loaded</strong> · Review and edit before sending");
}

function openWarPlan() {
  const progress = getLevelProgress({ points: state.points, onboardingCompleted: state.onboardingCompleted });
  const target = progress.next ?? progress.current;
  const pointGap = progress.pointsToNext;
  const weeklyPrompts = Math.min(20, Math.ceil(Math.min(pointGap, 60) / 3));
  const taskPointsNeeded = Math.max(0, pointGap - weeklyPrompts * 3);
  const weeklyTasks = Math.ceil(taskPointsNeeded / 5 / 3);
  const card = document.querySelector("#war-plan-card");
  card.innerHTML = `<header><span class="war-plan-icon">⚡</span><div><p class="eyebrow">Homies level coach</p><h2 id="war-plan-title">Your 3-week path to Level ${target.level} · ${target.name}</h2></div><span class="war-plan-gap">${formatPoints(pointGap)} pts to go</span></header>
    <p class="war-plan-intro">Based on your current mix, this plan balances ${weeklyPrompts} useful prompts and about ${weeklyTasks} verified tasks per week. Adjust it around your active clients—quality always beats farming points.</p>
    <div class="war-plan-weeks">
      <section><span>Every week</span><strong>${weeklyPrompts} prompts</strong><small>Planning, drafting and analysis</small></section>
      <section><span>Pipeline</span><strong>5 follow-ups · 4 listings</strong><small>Sent or logged through Homies</small></section>
      <section><span>Client work</span><strong>3 showings · 2 valuations</strong><small>Confirmed or completed outcomes</small></section>
      <section><span>Growth</span><strong>1 offer · 1 pitch · 2 reports/posts</strong><small>Round out the weekly target</small></section>
    </div>
    <footer><span>Projected finish: <strong>about 3 active weeks</strong></span><button class="button primary js-start-war-plan" type="button">Start week one with Homies</button></footer>`;
  card.hidden = false;
  window.location.hash = "#dashboard";
  window.setTimeout(() => card.scrollIntoView({ behavior: "smooth", block: "center" }), 80);
  showToast("<strong>War plan ready</strong> · Built from your real point gap and KPI mix");
}

function handleTryPrompt(template) {
  const input = document.querySelector("#prompt-input");
  if (!input.value.trim()) {
    usePromptTemplate(template);
    return;
  }
  pendingPrompt = template;
  document.querySelector("#prompt-dialog").showModal();
}

function showAchievementUnlock(unlocks) {
  const achievement = unlocks.at(-1);
  currentAchievement = achievement;
  const payoff = {
    1: "Your first win is on the board.", 5: "The loop is working—keep the momentum.", 10: "Double digits unlocked.", 20: "This is becoming a repeatable habit.", 50: "Serious momentum. The next badge is in sight.", 100: "Welcome to the Century Club.", 250: "Elite output, built one task at a time.", 500: "Titan status—an exceptional body of work.", 1000: "Legendary. Your next chapter is the leaderboard.",
  };
  document.querySelector("#achievement-dialog-badge").innerHTML = badgeMarkup(achievement);
  document.querySelector("#achievement-dialog-title").textContent = achievement.title;
  const earlier = unlocks.length > 1 ? ` ${unlocks.length - 1} earlier badge${unlocks.length > 2 ? "s" : ""} also unlocked.` : "";
  document.querySelector("#achievement-dialog-copy").textContent = `${shareSentence(achievement)} ${payoff[achievement.milestone]}${earlier}`;
  document.querySelector("#celebration-sparks").innerHTML = Array.from({ length: 14 }, (_, index) => `<i style="--i:${index}"></i>`).join("");
  document.querySelector("#achievement-dialog").showModal();
}

function bumpWeekly(key) {
  if (weeklySeries[key]) weeklySeries[key][weeklySeries[key].length - 1] += 1;
}

function addActivity(type) {
  let message;
  const previousCounts = achievementCounts();
  if (type === "prompt") {
    state.promptsSubmitted += 1;
    state.points += 1;
    bumpWeekly("promptsSubmitted");
    message = "<strong>+1 point</strong> · Accepted prompt recorded";
  } else {
    state.tasksCompleted += 1;
    state.taskCounts[type] = (state.taskCounts[type] ?? 0) + 1;
    state.points += 5;
    bumpWeekly("tasksCompleted");
    bumpWeekly(type);
    message = `<strong>+5 points</strong> · ${TASK_LABELS[type] ?? "Task"} completed`;
  }
  renderAll();
  const unlocks = getNewAchievementUnlocks(previousCounts, achievementCounts());
  if (unlocks.length) {
    showAchievementUnlock(unlocks);
  } else {
    const progress = type === "prompt" ? null : getAchievementProgress(type, state.taskCounts[type]);
    const echo = progress?.next ? ` · ${progress.count}/${progress.next.milestone} to ${progress.next.title}` : "";
    showToast(`${message}${echo}`);
  }
}

document.querySelectorAll(".js-open-progress").forEach((button) => {
  button.addEventListener("click", () => { window.location.hash = "#progress/overview"; });
});

document.querySelectorAll('[role="tab"]').forEach((tab) => {
  tab.addEventListener("click", () => { window.location.hash = `#progress/${tab.dataset.tab}`; });
  tab.addEventListener("keydown", (event) => {
    if (!["ArrowLeft", "ArrowRight"].includes(event.key)) return;
    const tabs = [...document.querySelectorAll('[role="tab"]')];
    const direction = event.key === "ArrowRight" ? 1 : -1;
    const next = tabs[(tabs.indexOf(tab) + direction + tabs.length) % tabs.length];
    next.focus();
    next.click();
  });
});

document.querySelector("#chart-period").addEventListener("change", renderChart);
document.querySelector("#leaderboard-metric").addEventListener("change", renderLeaderboard);
document.querySelector("#leaderboard-period").addEventListener("change", renderLeaderboard);
document.querySelector("#leaderboard-scope").addEventListener("change", renderLeaderboard);
document.querySelector("#simulate-button").addEventListener("click", () => addActivity(document.querySelector("#activity-select").value));
document.querySelector("#demo-composer").addEventListener("submit", (event) => {
  event.preventDefault();
  const input = document.querySelector("#prompt-input");
  if (!input.value.trim()) {
    input.focus();
    return;
  }
  input.value = "";
  addActivity("prompt");
});

document.addEventListener("click", (event) => {
  const removeKpi = event.target.closest("[data-remove-kpi]");
  if (removeKpi) {
    visibleKpis = visibleKpis.filter((key) => key !== removeKpi.dataset.removeKpi);
    saveVisibleKpis();
    renderScoreboard();
    showToast(`<strong>Metric removed</strong> · Add it back anytime from Add metric`);
    return;
  }
  const addKpi = event.target.closest("[data-add-kpi]");
  if (addKpi) {
    visibleKpis.push(addKpi.dataset.addKpi);
    saveVisibleKpis();
    renderScoreboard();
    showToast("<strong>Metric added</strong> · Your scoreboard is saved on this device");
    return;
  }
  const inviteButton = event.target.closest(".js-open-invite");
  if (inviteButton) {
    const org = partnerOrganizations[currentPartnerOrgId];
    document.querySelector("#invite-preview-logo").textContent = org.initials;
    document.querySelector("#invite-preview-name").textContent = `You’re invited to ${org.productName}`;
    document.querySelector("#partner-invite-dialog").showModal();
    return;
  }
  const shareButton = event.target.closest(".js-share-win");
  if (shareButton) {
    const achievement = achievementFor(shareButton.dataset.metric, Number(shareButton.dataset.milestone));
    openShareDialog(achievement);
    return;
  }
  const profileButton = event.target.closest(".js-open-profile");
  if (profileButton) {
    openProfileDialog(profileButton.dataset.profile);
    return;
  }
  const promptButton = event.target.closest(".try-prompt-button");
  if (promptButton) {
    document.querySelector("#profile-dialog").open && document.querySelector("#profile-dialog").close();
    handleTryPrompt(promptButton.dataset.prompt);
    return;
  }
  const closeButton = event.target.closest("[data-close-dialog]");
  if (closeButton) document.querySelector(`#${closeButton.dataset.closeDialog}`).close();
  const startPlan = event.target.closest(".js-start-war-plan");
  if (startPlan) usePromptTemplate("Help me execute week one of my Level 6 war plan. Turn these targets into a day-by-day checklist: 20 useful prompts, 5 follow-ups, 4 listings sent to buyers, 3 confirmed showings, 2 CMAs or home valuations, 1 offer, 1 listing presentation, and 2 market reports or social posts. Ask me which active clients and listings I want to prioritize before using any client data.");
});

document.querySelector("#add-metric-button").addEventListener("click", () => {
  const picker = document.querySelector("#metric-picker");
  picker.hidden = !picker.hidden;
  document.querySelector("#add-metric-button").setAttribute("aria-expanded", String(!picker.hidden));
});

document.querySelector("#partner-org-select").addEventListener("change", (event) => {
  currentPartnerOrgId = event.target.value;
  renderPartnerHub();
  showToast(`<strong>Context switched</strong> · Now viewing ${partnerOrganizations[currentPartnerOrgId].name}`);
});

document.querySelectorAll("[data-partner-view]").forEach((button) => {
  button.addEventListener("click", () => setPartnerView(button.dataset.partnerView));
});

document.querySelector("#partner-chart-metric").addEventListener("change", () => renderPartnerActivity(partnerOrganizations[currentPartnerOrgId]));
document.querySelector("#organization-ranking-mode").addEventListener("change", () => renderOrganizationRanking(partnerOrganizations[currentPartnerOrgId]));
document.querySelector("#member-status-filter").addEventListener("change", () => renderPartnerMembers(partnerOrganizations[currentPartnerOrgId]));

document.querySelector("#partner-invite-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const rawEmails = document.querySelector("#invite-emails").value.split(/[\n,;]/).map((email) => email.trim()).filter(Boolean);
  if (!rawEmails.length) return;
  const org = partnerOrganizations[currentPartnerOrgId];
  rawEmails.forEach((email, index) => {
    const localName = email.split("@")[0].replace(/[._-]+/g, " ").replace(/\b\w/g, (letter) => letter.toUpperCase());
    const initials = localName.split(/\s+/).map((part) => part[0]).join("").slice(0, 2).toUpperCase() || "N";
    org.members.push({ publicId: `pending-${Date.now()}-${index}`, name: localName || email, initials, memberships: [[org.name.replace(" concept", ""), org.id === "golfi" ? "team" : "coach"]], group: document.querySelector("#invite-cohort").value, week: "—", level: 1, status: "invited", note: "Invite pending" });
  });
  document.querySelector("#partner-invite-dialog").close();
  document.querySelector("#partner-invite-form").reset();
  setPartnerView("members");
  document.querySelector("#member-status-filter").value = "invited";
  renderPartnerMembers(org);
  showToast(`<strong>${rawEmails.length} invitation${rawEmails.length === 1 ? "" : "s"} created</strong> · Identity and KPI consent are accepted by each invitee`);
});

document.querySelector("#copy-invite-link-button").addEventListener("click", async () => {
  const inviteLink = `https://join.homiesai.com/${currentPartnerOrgId}-concept`;
  try { await navigator.clipboard.writeText(inviteLink); } catch { /* Clipboard may be unavailable in a prototype frame. */ }
  showToast("<strong>Invite link ready</strong> · Membership and sharing consent still require acceptance");
});

document.querySelector("#preview-support-button").addEventListener("click", () => {
  setPartnerView("members");
  document.querySelector("#member-status-filter").value = "support";
  renderPartnerMembers(partnerOrganizations[currentPartnerOrgId]);
  showToast("<strong>Private support queue</strong> · Showing members who may benefit from a check-in");
});

document.querySelector("#create-cohort-button").addEventListener("click", () => {
  const org = partnerOrganizations[currentPartnerOrgId];
  if (!org.cohorts.some((cohort) => cohort.name === "90-Day Listings Lab")) org.cohorts.push({ name: "90-Day Listings Lab", kind: "New cohort", members: 0, onPace: 0, goal: "Set after member consent", lead: "Unassigned" });
  renderPartnerCohorts(org);
  showToast("<strong>Cohort created</strong> · Add a lead, targets and consenting members next");
});

document.querySelectorAll("[data-brand-color]").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll("[data-brand-color]").forEach((item) => item.classList.toggle("selected", item === button));
    document.querySelector("#white-label-preview").style.setProperty("--preview-color", button.dataset.brandColor);
  });
});

document.querySelector("#powered-by-toggle").addEventListener("change", (event) => {
  document.querySelector("#powered-by-homies").textContent = event.target.checked ? "Powered by Homies" : "Securely powered by Homies";
});

document.querySelectorAll("[data-billing-mode]").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll("[data-billing-mode]").forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
    showToast(`<strong>${button.querySelector("strong").textContent}</strong> · Billing transition preview updated`);
  });
});

document.querySelector("#save-brand-button").addEventListener("click", () => showToast("<strong>Brand concept saved</strong> · Production publish will validate contrast, domains and recovery paths"));
document.querySelector("#preview-exit-button").addEventListener("click", () => document.querySelector("#member-exit-dialog").showModal());
document.querySelector("#exit-understanding").addEventListener("change", (event) => { document.querySelector("#simulate-exit-button").disabled = !event.target.checked; });
document.querySelector("#simulate-exit-button").addEventListener("click", () => {
  const coachNode = document.querySelector(".membership-node.coach");
  coachNode.textContent = "Ferry Alumni";
  coachNode.classList.add("ended");
  document.querySelector("#member-exit-dialog").close();
  showToast("<strong>Membership ended safely</strong> · Taylor kept Level 5, history, badges, integrations and the Golfi Team membership");
});

document.querySelector(".js-share-current").addEventListener("click", () => {
  document.querySelector("#achievement-dialog").close();
  openShareDialog(currentAchievement);
});

document.querySelector("#post-community-button").addEventListener("click", () => {
  const caption = document.querySelector("#share-caption").value.trim();
  const post = document.createElement("article");
  post.className = "feed-post achievement-post fresh-post";
  post.dataset.postType = "win";
  post.innerHTML = `<header class="feed-author"><button class="profile-avatar js-open-profile" data-profile="you" type="button">TM</button><div><button class="author-name js-open-profile" data-profile="you" type="button">Taylor M. <span class="micro-badge tier-${tierIndexFor(currentAchievement.milestone)}">${currentAchievement.milestone}</span></button><span>Toronto · Level 5 Operator · Just now</span></div><span class="post-kind">Verified win</span></header><div class="feed-body">${badgeMarkup(currentAchievement)}<div><p class="eyebrow">Achievement unlocked</p><h3>${currentAchievement.title}</h3><p>${escapeHtml(caption).replace(/\n/g, "<br>")}</p></div></div><footer class="feed-actions"><button class="reaction-button" type="button">🔥 <span>0</span></button><button type="button">💬 Reply</button><button type="button">•••</button></footer>`;
  document.querySelector("#community-feed").prepend(post);
  document.querySelector("#share-dialog").close();
  window.location.hash = "#progress/community";
  showToast("<strong>Win shared</strong> · Posted to the Homies community");
});

document.querySelector("#copy-caption-button").addEventListener("click", async () => {
  const caption = document.querySelector("#share-caption").value;
  try {
    await navigator.clipboard.writeText(caption);
    showToast("<strong>Copied</strong> · Share caption is on your clipboard");
  } catch {
    document.querySelector("#share-caption").select();
    showToast("<strong>Caption selected</strong> · Copy it with your keyboard");
  }
});

document.querySelectorAll("[data-share-destination]").forEach((button) => {
  button.addEventListener("click", async () => {
    const destination = button.dataset.shareDestination;
    const caption = document.querySelector("#share-caption").value;
    if (destination === "native" && navigator.share) {
      try { await navigator.share({ title: currentAchievement.title, text: caption }); } catch { /* User cancelled the OS share sheet. */ }
      return;
    }
    const label = destination === "linkedin" ? "LinkedIn badge package" : destination === "instagram" ? "9:16 Story card" : "Share package";
    showToast(`<strong>${label} ready</strong> · Production will export the verified card and link`);
  });
});

document.querySelectorAll("[data-prompt-choice]").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelector("#prompt-dialog").close();
    usePromptTemplate(pendingPrompt, button.dataset.promptChoice);
    pendingPrompt = "";
  });
});

document.querySelectorAll(".community-filter button").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".community-filter button").forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
    const label = button.textContent.trim().toLowerCase();
    const type = label === "wins" ? "win" : label === "prompts" ? "prompt" : label === "q&a" ? "question" : null;
    document.querySelectorAll("#community-feed > .feed-post").forEach((post) => { post.hidden = Boolean(type && post.dataset.postType !== type); });
  });
});

document.addEventListener("click", (event) => {
  const reaction = event.target.closest(".reaction-button");
  if (reaction) {
    const count = reaction.querySelector("span");
    const active = reaction.classList.toggle("active");
    count.textContent = Number(count.textContent) + (active ? 1 : -1);
    reaction.setAttribute("aria-pressed", String(active));
  }
  const follow = event.target.closest(".follow-button");
  if (follow) {
    const active = follow.classList.toggle("following");
    follow.textContent = active ? "Following" : "Follow";
    showToast(active ? "<strong>Following</strong> · Their useful posts will show up here" : "No longer following");
  }
});

document.querySelector("#create-post-button").addEventListener("click", () => showToast("<strong>Post composer framed</strong> · V1 supports wins, prompts, tips and questions"));
document.querySelector("#edit-pins-button").addEventListener("click", () => showToast("<strong>Badge loadout</strong> · Pin up to three achievements beside your name"));
document.querySelector("#coach-preview-button").addEventListener("click", () => showToast("<strong>Coach view framed</strong> · Cohorts, weekly targets, intervention alerts and exportable scorecards"));
document.querySelector("#war-plan-button").addEventListener("click", openWarPlan);

document.querySelectorAll("dialog").forEach((dialog) => {
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) dialog.close();
  });
});
window.addEventListener("hashchange", handleRoute);

/* ------------------------------------------------------------------ */
/* Accountability partner, coach reports, sharing controls and GCI     */
/* ------------------------------------------------------------------ */

const SHAREABLE_DATAPOINTS = [
  { key: "level_points", label: "Level, points & streak", icon: "tasks" },
  { key: "activity_graph", label: "365-day activity graph", icon: "report" },
  { key: "achievements", label: "Achievements & badges", icon: "presentation" },
  ...KPI_CATALOG.map((kpi) => ({ key: kpi.key, label: kpi.label, icon: kpi.icon })),
  { key: "avg_touches", label: "Avg follow-up attempts per client", icon: "touches" },
  { key: "gci", label: "GCI (gross commission income)", icon: "gci", defaultShared: false },
];

let sharingPrefs;
try {
  const saved = JSON.parse(localStorage.getItem("homies-sharing") ?? "null");
  sharingPrefs = saved && typeof saved === "object" && Array.isArray(saved.hidden)
    ? { master: saved.master !== false, hidden: saved.hidden }
    : { master: true, hidden: SHAREABLE_DATAPOINTS.filter((item) => item.defaultShared === false).map((item) => item.key) };
} catch {
  sharingPrefs = { master: true, hidden: ["gci"] };
}

function renderSharingGrid() {
  document.querySelector("#master-share-toggle").checked = sharingPrefs.master;
  document.querySelector("#master-share-copy").textContent = sharingPrefs.master
    ? "Sharing on · other members can see the data points below"
    : "Sharing off · your profile shows only your name and level";
  const grid = document.querySelector("#sharing-datapoint-grid");
  grid.classList.toggle("disabled", !sharingPrefs.master);
  grid.innerHTML = SHAREABLE_DATAPOINTS.map((item) => `
    <label class="sharing-datapoint ${sharingPrefs.hidden.includes(item.key) ? "off" : ""}">
      <span class="kpi-icon" aria-hidden="true"><svg viewBox="0 0 24 24">${iconPaths[item.icon]}</svg></span>
      <span class="sharing-datapoint-label">${item.label}${item.defaultShared === false ? "<small>Private by default</small>" : ""}</span>
      <input type="checkbox" data-share-key="${item.key}" ${sharingPrefs.hidden.includes(item.key) ? "" : "checked"} ${sharingPrefs.master ? "" : "disabled"}>
    </label>`).join("");
}

function openSharingDialog() {
  renderSharingGrid();
  document.querySelector("#sharing-dialog").showModal();
}

document.addEventListener("click", (event) => {
  if (event.target.closest(".js-open-sharing")) openSharingDialog();
});

document.querySelector("#master-share-toggle").addEventListener("change", (event) => {
  sharingPrefs.master = event.target.checked;
  renderSharingGrid();
});

document.querySelector("#sharing-datapoint-grid").addEventListener("change", (event) => {
  const key = event.target.dataset.shareKey;
  if (!key) return;
  sharingPrefs.hidden = event.target.checked
    ? sharingPrefs.hidden.filter((item) => item !== key)
    : [...new Set([...sharingPrefs.hidden, key])];
  event.target.closest(".sharing-datapoint").classList.toggle("off", !event.target.checked);
});

document.querySelector("#save-sharing-button").addEventListener("click", () => {
  localStorage.setItem("homies-sharing", JSON.stringify(sharingPrefs));
  document.querySelector("#sharing-dialog").close();
  const visibleCount = sharingPrefs.master ? SHAREABLE_DATAPOINTS.length - sharingPrefs.hidden.length : 0;
  showToast(`<strong>Sharing saved</strong> · ${visibleCount} of ${SHAREABLE_DATAPOINTS.length} data points visible to other Homies`);
});

function renderAccountability() {
  const status = document.querySelector("#partner-cta-status");
  const inviteButton = document.querySelector("#invite-partner-button");
  const manageButton = document.querySelector("#partner-manage-button");
  if (state.partner) {
    status.innerHTML = `<strong>Invitation sent to ${escapeHtml(state.partner.email)}</strong> · waiting for them to accept. You will each confirm what the other can see${state.partner.digest ? ", then Monday digests start automatically" : ""}.`;
    inviteButton.hidden = true;
    manageButton.hidden = false;
  } else {
    status.textContent = "Invite one trusted agent. You each choose exactly which numbers the other can see, and Homies keeps you both honest with a Monday digest.";
    inviteButton.hidden = false;
    manageButton.hidden = true;
  }
  const coachStatus = document.querySelector("#coach-report-status");
  const coachButton = document.querySelector("#coach-report-button");
  if (state.coachReport) {
    const cadenceCopy = { weekly: "every Monday 8am", biweekly: "every other Monday", monthly: "on the 1st of each month", once: "one-time send" };
    coachStatus.innerHTML = `<strong>${escapeHtml(state.coachReport.role)} report → ${escapeHtml(state.coachReport.email)}</strong> · ${cadenceCopy[state.coachReport.cadence]} · ${state.coachReport.included.length} data points`;
    coachButton.textContent = "Manage report";
  } else {
    coachStatus.textContent = "A clean weekly summary of the data points you pick—no inbox screenshots, no spreadsheet exports.";
    coachButton.textContent = "Set up a report";
  }
}

document.querySelector("#invite-partner-button").addEventListener("click", () => document.querySelector("#accountability-dialog").showModal());
document.querySelector("#partner-manage-button").addEventListener("click", () => document.querySelector("#accountability-dialog").showModal());

document.querySelector("#accountability-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const email = document.querySelector("#partner-email").value.trim();
  if (!email) return;
  const shares = [...document.querySelectorAll("#partner-share-grid input:checked")].map((input) => input.dataset.share);
  state.partner = { email, shares, digest: document.querySelector("#partner-digest-toggle").checked, status: "invited" };
  document.querySelector("#accountability-dialog").close();
  renderAccountability();
  showToast(`<strong>Partner invited</strong> · ${escapeHtml(email)} will confirm the pairing and their own sharing list`);
});

function updateReportPreview() {
  const included = [...document.querySelectorAll("#report-share-grid input:checked")].map((input) => input.closest("label").textContent.trim());
  const cadence = document.querySelector("#report-cadence");
  const touches = (state.taskCounts.follow_up / state.activeClients).toFixed(1);
  document.querySelector("#report-preview").innerHTML = included.length
    ? `<p class="eyebrow">Preview · ${cadence.options[cadence.selectedIndex].text}</p><p><strong>Taylor M. — week of Jul 6:</strong> ${formatPoints(weeklySeries.tasksCompleted.at(-1))} verified tasks · ${formatPoints(weeklySeries.follow_up.at(-1))} follow-ups (${touches} avg touches/client) · ${formatPoints(weeklySeries.appointment.at(-1))} appointments · on pace for Level 6 in ~3 weeks.</p><small>${included.length} data point group${included.length === 1 ? "" : "s"} included. GCI stays out unless you check it.</small>`
    : '<p><strong>Nothing selected.</strong> Pick at least one data point group to send.</p>';
}

document.querySelector("#coach-report-button").addEventListener("click", () => {
  updateReportPreview();
  document.querySelector("#coach-report-dialog").showModal();
});
document.querySelector("#coach-report-form").addEventListener("change", updateReportPreview);

document.querySelector("#coach-report-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const email = document.querySelector("#report-email").value.trim();
  if (!email) return;
  const included = [...document.querySelectorAll("#report-share-grid input:checked")].map((input) => input.dataset.report);
  if (!included.length) {
    showToast("<strong>Pick at least one data point</strong> · The report needs something to say");
    return;
  }
  state.coachReport = { email, role: document.querySelector("#report-role").value, cadence: document.querySelector("#report-cadence").value, included };
  document.querySelector("#coach-report-dialog").close();
  renderAccountability();
  showToast(state.coachReport.cadence === "once"
    ? `<strong>Report sent</strong> · ${escapeHtml(email)} received your verified scorecard`
    : `<strong>Report scheduled</strong> · ${escapeHtml(email)} gets your verified scorecard automatically`);
});

const GCI_SCAN_ESTIMATES = { 2022: 148200, 2023: 164750, 2024: 189000, 2025: 214300 };

document.querySelector("#gci-manual-button").addEventListener("click", () => document.querySelector("#gci-dialog").showModal());
document.querySelector("#gci-scan-button").addEventListener("click", () => {
  document.querySelector("#gci-dialog").showModal();
  document.querySelector("#gci-consent").focus();
});

document.querySelector("#gci-consent").addEventListener("change", (event) => {
  document.querySelector("#gci-scan-start").disabled = !event.target.checked;
});

document.querySelector("#gci-manual-save").addEventListener("click", () => {
  const year = Number(document.querySelector("#gci-manual-year").value);
  const raw = document.querySelector("#gci-manual-amount").value.replace(/[^0-9.]/g, "");
  const amount = Number(raw);
  if (!raw || !Number.isFinite(amount) || amount <= 0) {
    showToast("<strong>Enter an amount</strong> · e.g. $215,000");
    return;
  }
  state.gci = [...state.gci.filter((record) => record.year !== year), { year, amount, source: "manual", note: "Entered by you" }];
  document.querySelector("#gci-manual-amount").value = "";
  renderGci();
  showToast(`<strong>${year} GCI saved</strong> · ${formatMoney(amount)} · private until you share it`);
});

document.querySelector("#gci-scan-start").addEventListener("click", () => {
  const years = [...document.querySelectorAll("#gci-scan-years input:checked")].map((input) => Number(input.value));
  if (!years.length) {
    showToast("<strong>Pick at least one year</strong> · The scan needs a date range");
    return;
  }
  const progress = document.querySelector("#gci-scan-progress");
  progress.hidden = false;
  const steps = [
    "Searching your connected inbox for commission statements…",
    "Matching brokerage EFT / trust transfer notices…",
    "Reading tax slips (T4A / 1099) for the selected years…",
    `Drafting totals for ${years.join(", ")}…`,
  ];
  progress.innerHTML = "";
  steps.forEach((step, index) => {
    window.setTimeout(() => {
      progress.innerHTML += `<p>✓ ${step}</p>`;
      if (index === steps.length - 1) {
        window.setTimeout(() => {
          years.forEach((year) => {
            const amount = GCI_SCAN_ESTIMATES[year] ?? 150000;
            state.gci = [...state.gci.filter((record) => record.year !== year), { year, amount, source: "email_scan", note: "Confirmed from email scan" }];
          });
          renderGci();
          document.querySelector("#gci-dialog").close();
          progress.hidden = true;
          document.querySelector("#gci-consent").checked = false;
          document.querySelector("#gci-scan-start").disabled = true;
          showToast(`<strong>GCI history drafted</strong> · ${years.length} year${years.length === 1 ? "" : "s"} added from your email · review anytime`);
        }, 700);
      }
    }, 550 * (index + 1));
  });
});

renderChartLegend();
renderChart();
renderAll();
handleRoute();
