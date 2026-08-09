import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { InterviewProvider } from "./context/InterviewContext";
import MainLayout from "./layouts/MainLayout";
import Candidates from "./pages/Candidates";
import Feedback from "./pages/Feedback";
import Interview from "./pages/Interview";
import Landing from "./pages/Landing";
import Setup from "./pages/Setup";

export default function App() {
  return (
    <InterviewProvider>
      <BrowserRouter>
        <Routes>
          <Route element={<MainLayout />}>
            <Route index element={<Landing />} />
            <Route path="candidates" element={<Candidates />} />
            <Route path="setup" element={<Setup />} />
            <Route path="interview" element={<Interview />} />
            <Route path="feedback" element={<Feedback />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </InterviewProvider>
  );
}
