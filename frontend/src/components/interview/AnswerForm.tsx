import type { FormEvent } from "react";

type AnswerFormProps = {
  value: string;
  onChange: (value: string) => void;
  onSubmit: () => void;
  isLoading: boolean;
  disabled?: boolean;
};

export function AnswerForm({ value, onChange, onSubmit, isLoading, disabled }: AnswerFormProps) {
  const handleSubmit = (event: FormEvent) => {
    event.preventDefault();
    if (!value.trim() || isLoading || disabled) return;
    onSubmit();
  };

  return (
    <form className="answer" onSubmit={handleSubmit}>
      <label htmlFor="answer">Your answer</label>
      <textarea
        id="answer"
        value={value}
        onChange={(event) => onChange(event.target.value)}
        placeholder="Explain your thinking clearly. Examples and trade-offs make your answer stronger."
        disabled={isLoading || disabled}
      />
      <button type="submit" className="primary" disabled={isLoading || disabled || !value.trim()}>
        {isLoading ? "Evaluating your answer…" : "Submit answer →"}
      </button>
    </form>
  );
}
