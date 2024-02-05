#!/bin/sh

# Iniciamos proyecto

npm = create vite@latest . -- --template react

echo "import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
    plugin: [react()],
    server: {
        host: true,
        port: 8000,
        watch: {
            usePolling: true
        }
    }
})" > vite.config.js