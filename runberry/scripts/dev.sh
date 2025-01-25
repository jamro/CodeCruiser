#!/bin/sh

cd "$(dirname "$0")/../backend"
echo "Starting the backend..."
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Start the frontend
echo "Starting the frontend..."
cd "../frontend"
npm start &
FRONTEND_PID=$!

# Wait for user to stop the script
echo "Backend PID: $BACKEND_PID, Frontend PID: $FRONTEND_PID"
echo "Press [Ctrl+C] to stop the servers."

# Handle termination signals
trap "echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT TERM

# Keep the script running to keep both servers alive
wait