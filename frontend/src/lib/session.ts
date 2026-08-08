const SESSION_KEY = "interview:sessionId";

export function createSessionId(): string {
  return crypto.randomUUID();
}

export function getSessionId(): string | null {
  return sessionStorage.getItem(SESSION_KEY);
}

export function setSessionId(sessionId: string): void {
  sessionStorage.setItem(SESSION_KEY, sessionId);
}

export function clearSessionId(): void {
  sessionStorage.removeItem(SESSION_KEY);
}

export function startFreshSession(): string {
  const sessionId = createSessionId();
  setSessionId(sessionId);
  return sessionId;
}

export function getOrCreateSessionId(): string {
  return getSessionId() ?? startFreshSession();
}
