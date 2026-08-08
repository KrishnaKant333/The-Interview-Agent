import { InterviewProgress } from "./InterviewProgress";

type InterviewSidebarProps = {
  questionNumber: number;
  totalQuestions: number;
};

export function InterviewSidebar({ questionNumber, totalQuestions }: InterviewSidebarProps) {
  return (
    <aside className="sidebar">
      <small>INTERVIEW PROGRESS</small>
      <InterviewProgress current={questionNumber} total={totalQuestions} />
      <div>
        <small>SESSION</small>
        <p>
          Question {questionNumber} of {totalQuestions}
        </p>
      </div>
      <div>
        <small>PERSONALIZATION</small>
        <p>Based on completed curriculum days and focus areas.</p>
      </div>
    </aside>
  );
}
