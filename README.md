# Reinforcement Learning: Moving a Red Box 🚀

## 📌 Project Overview

This is my first reinforcement learning project where I train an agent to move a red box (100x100 pixels) from the left corner (x=0) to the right side (x=800) of the screen. The environment is built using PyGame and wrapped as a Gymnasium environment, with training performed using Stable-Baselines3.

## 🛠️ Technologies Used

- **Python 3.11**
- **Gymnasium** (OpenAI Gym's successor)
- **Stable-Baselines3** (PPO algorithm)
- **PyGame** (for rendering)

## 🏗️ Environment Details

### Observation Space

- Box position (x-coordinate)

### Action Space

- Discrete actions:
    - 0: Stay still
    - 1: Mode left
    - 2: Move right

### Reward Function

- Positive reward for moving right
- Negative reward for moving left
- Negative reward for do nothing
- Positive reward if goal is achieved in less than 150 steps
- Negative reward if goal is achieved in more than 150 steps
- Reduction of the fine for shortening the distance

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Training the Agent

```bash
python3.11 main.py train
```

### Testing the Trained Agent

```bash
python3.11 main.py
```

## 📊 Training Results

After 20,000 timesteps, the agent should learn to:

- Efficiently move the box to the right
- Avoid unnecessary movements
- Consistently reach the goal position

## 🧠 What I Learned

- How to create custom Gymnasium environments
- Basics of reinforcement learning with Stable-Baselines3
- The importance of reward shaping
- How to visualize agent behavior with PyGame

## 📂 Project Structure

```
BoxRL/
├── tensorboard_logs/
├── model/
├── requirements.txt
├── box_env.py
├── main.py
├── LICENSE
└── README.md
```

## 🤝 Contributing

This is a learning project, but suggestions are welcome! If you have ideas for improvement:

1. Fork the repository

2. Create your feature branch

3. Commit your changes

4. Push to the branch

5. Open a pull request

## 📜 License

GNU GENERAL PUBLIC LICENSE

---

🎉 **Happy RL Learning!** Feel free to star ⭐ this repo if you find it helpful for your own learning journey.
