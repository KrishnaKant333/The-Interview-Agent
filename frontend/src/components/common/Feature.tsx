type FeatureProps = {
  title: string;
  text: string;
};

export function Feature({ title, text }: FeatureProps) {
  return (
    <div className="feature">
      <b>{title}</b>
      <span>{text}</span>
    </div>
  );
}
