# 🐢 ROS 2 Practices - Shahid Ahamed Hasib

This repository contains ROS 2 (Robot Operating System 2) practice projects using Python.  
Currently, it includes a minimal ROS 2 workspace with a publisher-subscriber example package named `my_first_pkg`.

---

## 📁 Project Structure

ros2_ws/ ├── src/ │ └── my_first_pkg/ │ ├── my_first_pkg/ │ │ ├── talker_py.py │ │ ├── listener_py.py │ │ └── init.py │ ├── package.xml │ ├── setup.py │ ├── setup.cfg │ ├── CMakeLists.txt │ └── resource/ │ └── my_first_pkg


---

## 📦 Package: `my_first_pkg`

A basic Python ROS 2 package demonstrating:

- A **publisher node** (`talker_py`) that publishes messages to `/chatter`
- A **subscriber node** (`listener_py`) that listens to `/chatter`

### ✅ Dependencies

- `rclpy`
- `std_msgs`

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/shahidhasib586/Ros2_practices.git
cd Ros2_practices
Absolutely! Here's a ready-to-use **`README.md`** file for your GitHub repo [`Ros2_practices`](https://github.com/shahidhasib586/Ros2_practices), covering your ROS 2 workspace and your first Python package `my_first_pkg`.

You can paste this directly into:

```bash
~/ros2_ws/README.md
```

---

## 📄 `README.md` (Full Version):

```markdown
# 🐢 ROS 2 Practices - Shahid Ahamed Hasib

This repository contains ROS 2 (Robot Operating System 2) practice projects using Python.  
Currently, it includes a minimal ROS 2 workspace with a publisher-subscriber example package named `my_first_pkg`.

---

## 📁 Project Structure

```
ros2_ws/
├── src/
│   └── my_first_pkg/
│       ├── my_first_pkg/
│       │   ├── talker_py.py
│       │   ├── listener_py.py
│       │   └── __init__.py
│       ├── package.xml
│       ├── setup.py
│       ├── setup.cfg
│       ├── CMakeLists.txt
│       └── resource/
│           └── my_first_pkg
```

---

## 📦 Package: `my_first_pkg`

A basic Python ROS 2 package demonstrating:

- A **publisher node** (`talker_py`) that publishes messages to `/chatter`
- A **subscriber node** (`listener_py`) that listens to `/chatter`

### ✅ Dependencies

- `rclpy`
- `std_msgs`

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/shahidhasib586/Ros2_practices.git
cd Ros2_practices
```

### 2. Build the workspace

```bash
colcon build
source install/setup.bash
```

### 3. Run the publisher

```bash
ros2 run my_first_pkg talker_py
```

### 4. In a new terminal, run the subscriber

```bash
source install/setup.bash
ros2 run my_first_pkg listener_py
```

---

## 📚 Learn More

This workspace was created while learning and practicing:
- ROS 2 workspace setup
- Python packages (`ament_python`)
- Nodes, publishers, subscribers
- Package publishing on GitHub

---

## 📌 Author

**Shahid Ahamed Hasib**  
🎓 Erasmus Mundus Scholar  
📬 shahidhasib586@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/shahidhasib586)

---

## 📝 License

This project is licensed under the **Apache-2.0 License**.
```

---

Let me know if you want a shorter version, or want to include badges, gifs, or a turtlesim drawing demo section later.
