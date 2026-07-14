/**
 * Framework-agnostic gamification rules for Homies.
 *
 * The intentionally small scoring surface is the product contract:
 *   - one accepted user prompt = 1 point
 *   - one successfully completed workflow task = 5 points
 *   - onboarding is a gate for Level 2, not a repeatable source of points
 *
 * Task types drive analytics and metric-specific leaderboards, but every completed
 * task is worth the same amount. This makes the system easy to explain and prevents
 * the product from steering agents toward whichever workflow happens to pay more.
 */

export const POINTS = Object.freeze({
  prompt_submitted: 1,
  task_completed: 5,
});

export const POINT_POLICY = Object.freeze({
  promptDailyCap: 20,
  version: "v1",
});

export const TASK_TYPES = Object.freeze([
  "offer",
  "cma",
  "follow_up",
  "showing",
  "appointment",
  "crm_contact",
  "listing_presentation",
  "listing_sent",
  "market_report",
  "newsletter",
  "social_post",
  "dm_sent",
  "marketing_content",
  "deal_analysis",
]);

// Producers may continue to send the old event name while backends migrate.
// It rolls into the same user-visible CMA & home valuation counter.
export const TASK_ALIASES = Object.freeze({ home_evaluation: "cma" });

export const TASK_LABELS = Object.freeze({
  offer: "Offers",
  cma: "CMAs & home valuations",
  follow_up: "Follow-ups",
  showing: "Showings booked",
  appointment: "Appointments booked",
  crm_contact: "CRM contacts added",
  listing_presentation: "Listing presentations",
  listing_sent: "Listings sent to buyers",
  market_report: "Market reports sent",
  newsletter: "Newsletters sent",
  social_post: "Social posts published",
  dm_sent: "DMs sent",
  marketing_content: "Marketing assets",
  deal_analysis: "Deals analyzed",
});

export const ACHIEVEMENT_MILESTONES = Object.freeze([1, 5, 10, 20, 50, 100, 250, 500, 1000]);

export const ACHIEVEMENT_TIERS = Object.freeze([
  { milestone: 1, tier: "First Spark", rarity: "Copper", shape: "coin", color: "#b87345" },
  { milestone: 5, tier: "Quest Starter", rarity: "Bronze", shape: "pentagon", color: "#aa7439" },
  { milestone: 10, tier: "Momentum Maker", rarity: "Silver", shape: "shield", color: "#71829b" },
  { milestone: 20, tier: "Power Player", rarity: "Cobalt", shape: "diamond", color: "#4169a8" },
  { milestone: 50, tier: "Vanguard", rarity: "Gold", shape: "crest", color: "#c6922f" },
  { milestone: 100, tier: "Centurion", rarity: "Platinum", shape: "medallion", color: "#8c959f" },
  { milestone: 250, tier: "Elite", rarity: "Amethyst", shape: "crown", color: "#8468c9" },
  { milestone: 500, tier: "Titan", rarity: "Obsidian", shape: "winged", color: "#3f434d" },
  { milestone: 1000, tier: "Legend", rarity: "Iridescent", shape: "sigil", color: "#d85a30" },
]);

export const ACHIEVEMENT_METRICS = Object.freeze({
  prompts_submitted: {
    label: "Prompts submitted",
    icon: "message",
    titles: ["First Ask", "Prompt Starter", "Ten Questions", "Workflow Explorer", "Prompt Power", "Century Conversation", "AI Operator", "Prompt Titan", "Prompt Legend"],
  },
  tasks_completed: {
    label: "AI tasks completed",
    icon: "checklist",
    titles: ["First Assist", "Task Starter", "Double-Digit Doer", "Workflow Builder", "Work Engine", "Century Shipper", "Execution Elite", "Task Titan", "Work Legend"],
  },
  offer: {
    label: "Offers",
    icon: "document",
    titles: ["Inked In", "Offer Scout", "Deal Drafter", "Contract Crafter", "Offer Engine", "Offer Centurion", "Deal Architect", "Offer Titan", "Ink Legend"],
  },
  cma: {
    label: "CMAs & home valuations",
    icon: "chart",
    titles: ["Comp Scout", "Market Mapper", "Pricing Pathfinder", "Comp Crafter", "Market Decoder", "Market Centurion", "Pricing Architect", "Comp Titan", "CMA Legend"],
  },
  follow_up: {
    label: "Follow-ups",
    icon: "loop",
    titles: ["First Touch", "Conversation Starter", "Follow-Up Flow", "Connection Keeper", "Relationship Builder", "Nurture Centurion", "Pipeline Guardian", "Connection Titan", "Follow-Up Legend"],
  },
  showing: {
    label: "Showings booked",
    icon: "key",
    titles: ["Door Opener", "Tour Starter", "Key Keeper", "Showing Navigator", "Tour Captain", "Open-Door Centurion", "Showing Commander", "Keymaster", "Tour Legend"],
  },
  appointment: {
    label: "Appointments booked",
    icon: "calendar",
    titles: ["Calendar Click", "Meeting Maker", "Calendar Climber", "Appointment Ace", "Calendar Captain", "Century Scheduled", "Calendar Commander", "Meeting Titan", "Booking Legend"],
  },
  crm_contact: {
    label: "Contacts engaged",
    icon: "people",
    titles: ["First Connection", "Network Seed", "Contact Builder", "Relationship Mapper", "Network Builder", "Century of Connections", "Network Architect", "Network Titan", "Network Legend"],
  },
  listing_presentation: {
    label: "Listing presentations",
    icon: "presentation",
    titles: ["First Pitch", "Pitch Builder", "Deck Dealer", "Listing Closer", "Presentation Pro", "Century Stage", "Pitch Architect", "Listing Titan", "Pitch Legend"],
  },
  listing_sent: {
    label: "Listings sent",
    icon: "send",
    titles: ["First Match", "Buyer Scout", "Listing Curator", "Match Maker", "Inventory Guide", "Century Match", "Home Hunter Elite", "Listing Titan", "Match Legend"],
  },
  market_report: {
    label: "Market reports sent",
    icon: "report",
    titles: ["First Signal", "Market Messenger", "Trend Tracker", "Insight Operator", "Market Signal", "Century Brief", "Insight Architect", "Report Titan", "Market Oracle"],
  },
  newsletter: {
    label: "Newsletters sent",
    icon: "mail",
    titles: ["First Edition", "Inbox Starter", "Weekly Voice", "Audience Builder", "Newsletter Engine", "Century Publisher", "Editorial Elite", "Inbox Titan", "Publisher Legend"],
  },
  social_post: {
    label: "Social posts",
    icon: "megaphone",
    titles: ["Creator Mode", "Content Spark", "Campaign Crafter", "Brand Builder", "Content Engine", "Studio Century", "Marketing Engine", "Brand Titan", "Creator Legend"],
  },
  dm_sent: {
    label: "DMs sent",
    icon: "message",
    titles: ["First DM", "Conversation Spark", "Inbox Opener", "DM Driver", "Outreach Engine", "Century Sender", "Conversation Architect", "DM Titan", "Inbox Legend"],
  },
});

export const LEVELS = Object.freeze([
  { level: 1, name: "Starter", minimumPoints: 0, requirement: "Create your account" },
  { level: 2, name: "Explorer", minimumPoints: 0, requiresOnboarding: true, requirement: "Finish onboarding" },
  { level: 3, name: "Connector", minimumPoints: 150, requirement: "Earn 150 activity points" },
  { level: 4, name: "Builder", minimumPoints: 400, requirement: "Earn 400 activity points" },
  { level: 5, name: "Operator", minimumPoints: 800, requirement: "Earn 800 activity points" },
  { level: 6, name: "Producer", minimumPoints: 1350, requirement: "Earn 1,350 activity points" },
  { level: 7, name: "Accelerator", minimumPoints: 2100, requirement: "Earn 2,100 activity points" },
  { level: 8, name: "Rainmaker", minimumPoints: 3100, requirement: "Earn 3,100 activity points" },
  { level: 9, name: "Elite", minimumPoints: 4400, requirement: "Earn 4,400 activity points" },
  { level: 10, name: "Homies Legend", minimumPoints: 6000, requirement: "Earn 6,000 activity points" },
]);

export function pointsFromTotals({ pointEligiblePrompts = 0, tasksCompleted = 0 } = {}) {
  assertNonNegativeInteger(pointEligiblePrompts, "pointEligiblePrompts");
  assertNonNegativeInteger(tasksCompleted, "tasksCompleted");
  return pointEligiblePrompts * POINTS.prompt_submitted + tasksCompleted * POINTS.task_completed;
}

export function getLevelProgress({ points = 0, onboardingCompleted = false } = {}) {
  assertNonNegativeInteger(points, "points");

  if (!onboardingCompleted) {
    return {
      current: LEVELS[0],
      next: LEVELS[1],
      progressPercent: 0,
      pointsIntoLevel: 0,
      pointsToNext: 0,
      gate: "onboarding",
      isMaxLevel: false,
    };
  }

  const eligible = LEVELS.filter(
    (candidate) => candidate.level === 1 || candidate.level === 2 || points >= candidate.minimumPoints,
  );
  const current = eligible.at(-1);
  const next = LEVELS.find((candidate) => candidate.level === current.level + 1) ?? null;

  if (!next) {
    return {
      current,
      next: null,
      progressPercent: 100,
      pointsIntoLevel: points - current.minimumPoints,
      pointsToNext: 0,
      gate: null,
      isMaxLevel: true,
    };
  }

  const span = Math.max(1, next.minimumPoints - current.minimumPoints);
  const pointsIntoLevel = Math.max(0, points - current.minimumPoints);
  return {
    current,
    next,
    progressPercent: Math.min(100, Math.round((pointsIntoLevel / span) * 100)),
    pointsIntoLevel,
    pointsToNext: Math.max(0, next.minimumPoints - points),
    gate: null,
    isMaxLevel: false,
  };
}

export function summarizeEvents(events) {
  if (!Array.isArray(events)) throw new TypeError("events must be an array");

  const seen = new Set();
  const uniqueEvents = [];
  for (const event of events) {
    if (!event || typeof event !== "object") continue;
    if (!event.id || seen.has(event.id)) continue;
    seen.add(event.id);
    uniqueEvents.push(event);
  }
  uniqueEvents.sort((a, b) => String(a.occurredAt ?? "").localeCompare(String(b.occurredAt ?? "")));

  const taskCounts = Object.fromEntries(TASK_TYPES.map((type) => [type, 0]));
  let promptsSubmitted = 0;
  let pointEligiblePrompts = 0;
  let tasksCompleted = 0;
  let pointEligibleTasks = 0;
  let onboardingCompleted = false;
  const promptPointsByDay = new Map();

  for (const event of uniqueEvents) {
    if (event.type === "onboarding.completed") {
      onboardingCompleted = true;
    } else if (event.type === "prompt.submitted") {
      promptsSubmitted += 1;
      const day = typeof event.occurredAt === "string" ? event.occurredAt.slice(0, 10) : "unknown";
      const pointsToday = promptPointsByDay.get(day) ?? 0;
      if (onboardingCompleted && event.scoreEligible !== false && pointsToday < POINT_POLICY.promptDailyCap) {
        promptPointsByDay.set(day, pointsToday + 1);
        pointEligiblePrompts += 1;
      }
    } else if (event.type === "task.completed" && TASK_TYPES.includes(TASK_ALIASES[event.taskType] ?? event.taskType)) {
      const taskType = TASK_ALIASES[event.taskType] ?? event.taskType;
      tasksCompleted += 1;
      taskCounts[taskType] += 1;
      if (onboardingCompleted && event.scoreEligible !== false) pointEligibleTasks += 1;
    }
  }

  const points = pointsFromTotals({ pointEligiblePrompts, tasksCompleted: pointEligibleTasks });
  return {
    promptsSubmitted,
    pointEligiblePrompts,
    tasksCompleted,
    pointEligibleTasks,
    onboardingCompleted,
    taskCounts,
    points,
    level: getLevelProgress({ points, onboardingCompleted }),
  };
}

export function rankLeaderboard(entries, metric = "points") {
  if (!Array.isArray(entries)) throw new TypeError("entries must be an array");
  const supportedMetrics = new Set(["points", "promptsSubmitted", "tasksCompleted", ...TASK_TYPES, ...Object.keys(TASK_ALIASES)]);
  if (!supportedMetrics.has(metric)) throw new RangeError(`Unsupported leaderboard metric: ${metric}`);

  const valueFor = (entry) => {
    if (metric in TASK_ALIASES) return Number(entry.taskCounts?.[TASK_ALIASES[metric]]) || 0;
    if (metric in entry) return Number(entry[metric]) || 0;
    return Number(entry.taskCounts?.[metric]) || 0;
  };

  const sorted = entries
    .map((entry, originalIndex) => ({ ...entry, value: valueFor(entry), originalIndex }))
    .sort((a, b) => b.value - a.value || String(a.displayName).localeCompare(String(b.displayName)));

  let previousValue = null;
  let previousRank = 0;
  return sorted.map((entry, index) => {
    const rank = previousValue === entry.value ? previousRank : index + 1;
    previousValue = entry.value;
    previousRank = rank;
    const { originalIndex: _originalIndex, ...publicEntry } = entry;
    return { ...publicEntry, rank };
  });
}

export function getAchievementProgress(metric, count = 0) {
  if (!(metric in ACHIEVEMENT_METRICS)) throw new RangeError(`Unsupported achievement metric: ${metric}`);
  assertNonNegativeInteger(count, "count");

  const definition = ACHIEVEMENT_METRICS[metric];
  const catalog = ACHIEVEMENT_TIERS.map((tier, index) => ({
    ...tier,
    metric,
    metricLabel: definition.label,
    title: definition.titles[index],
  }));
  const earned = catalog.filter((achievement) => count >= achievement.milestone);
  const current = earned.at(-1) ?? null;
  const next = catalog.find((achievement) => count < achievement.milestone) ?? null;
  const currentFloor = current?.milestone ?? 0;
  const nextTarget = next?.milestone ?? currentFloor;
  const progressPercent = next
    ? Math.min(100, Math.round(((count - currentFloor) / Math.max(1, nextTarget - currentFloor)) * 100))
    : 100;

  return {
    metric,
    metricLabel: definition.label,
    count,
    catalog,
    earned,
    current,
    next,
    progressPercent,
    remaining: next ? Math.max(0, next.milestone - count) : 0,
    isMaxTier: next === null,
  };
}

export function getNewAchievementUnlocks(previousCounts = {}, nextCounts = {}) {
  return Object.keys(ACHIEVEMENT_METRICS).flatMap((metric) => {
    const previous = Number(previousCounts[metric]) || 0;
    const next = Number(nextCounts[metric]) || 0;
    if (next <= previous) return [];
    return getAchievementProgress(metric, next).catalog.filter(
      (achievement) => achievement.milestone > previous && achievement.milestone <= next,
    );
  });
}

export function formatPoints(value) {
  return new Intl.NumberFormat("en-CA").format(value);
}

function assertNonNegativeInteger(value, label) {
  if (!Number.isInteger(value) || value < 0) {
    throw new RangeError(`${label} must be a non-negative integer`);
  }
}
