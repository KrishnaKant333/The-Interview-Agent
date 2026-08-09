import type { InterviewRequest, InterviewResponse } from "../types";

const baseURL = (import.meta.env.VITE_API_BASE_URL ?? "").replace(/\/$/, "");

function interviewUrl(): string {
  return `${baseURL}/api/interview`;
}

export async function postInterview(request: InterviewRequest): Promise<InterviewResponse> {
  const url = interviewUrl();

  // TEMP DEBUG — remove after verifying live API mode
  console.log("[postInterview] called", { url, request });

  let response: Response;

  try {
    response = await fetch(interviewUrl(), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(request),
    });
  } catch {
    throw new Error("Network error. Check your connection and try again.");
  }

  let data: unknown;
  try {
    data = await response.json();
  } catch {
    throw new Error("Invalid response from the interview service.");
  }

  if (!response.ok) {
    const detail =
      data && typeof data === "object" && "detail" in data
        ? String((data as { detail: unknown }).detail)
        : `Request failed (${response.status})`;
    throw new Error(detail);
  }

  const parsed = data as InterviewResponse;
  if (!parsed || typeof parsed.reply !== "string" || typeof parsed.done !== "boolean") {
    throw new Error("Empty or invalid response from the interview service.");
  }

  return parsed;
}
