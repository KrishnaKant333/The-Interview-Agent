import type { InterviewRequest, InterviewResponse } from "../types";
import { apiClient } from "./api";

export async function postInterview(request: InterviewRequest): Promise<InterviewResponse> {
  const { data } = await apiClient.post<InterviewResponse>("/api/interview", request);

  if (!data || typeof data.reply !== "string" || typeof data.done !== "boolean") {
    throw new Error("Empty or invalid response from the interview service.");
  }

  return data;
}
