import path from "path"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"
import tailwindcss from "@tailwindcss/vite" // 1. Import Tailwind

export default defineConfig({
  plugins: [react(), tailwindcss()], // 2. Add to plugins array
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"), // 3. Configure the path alias
    },
  },
})
