type InterviewProgressProps = {
  current: number;
  total: number;
};

export function InterviewProgress({ current, total }: InterviewProgressProps) {
  return (
    <div className="dots">
      {Array.from({ length: total }, (_, index) => (
        <i className={index < current ? "done" : ""} key={index} />
      ))}
    </div>
  );
}
