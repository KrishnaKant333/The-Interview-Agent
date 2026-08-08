export function LoadingState({ message }: { message: string }) {
  return (
    <div className="status-message" role="status" aria-live="polite">
      <span className="status-spinner" aria-hidden="true" />
      <p>{message}</p>
    </div>
  );
}
