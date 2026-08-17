# Axon Curriculum Specification

## Educational Mission
Axon bridges high school mathematics and physics into modern machine learning, large language models, physical electromechanics, autonomous robotics (FIRST Robotics Competition / FRC), and agentic decision systems.

## Pedagogical Rules
1. **Paced & Approachable**: Build each concept step-by-step from everyday physical and software intuition. Avoid dense jargon dumps.
2. **Everyday FRC & Robotics Scenarios**: Ground every concept in a real robot challenge (e.g. reef distances, joystick steering, sensor jitter, elevator chains, shooter ballistics, swerve twist) before introducing formal equations.
3. **Code-First, in the Language of the Domain**: Every concept is explained through clean, boilerplate-free code with descriptive variable names. The language follows the subject matter, because the goal is for the reader to recognise the code when they meet it in the wild:
   * **Robotics concepts → Java & WPILib.** First-principles Java, paired with the production WPILib class that replaces it (`Translation2d`, `Pose2d`, `Rotation2d`, `MathUtil`, `TrapezoidProfile`, `Matrix`).
   * **Machine learning and LLM concepts → Python.** A from-scratch implementation in plain Python that shows the mechanism with nothing hidden, paired with the **PyTorch** equivalent that a practitioner would actually write.
   * **Mathematical foundations → whichever consumer the concept serves.** A concept feeding swerve kinematics is Java; one feeding gradient descent is Python. Where a concept genuinely serves both, show both.
4. **"Math!" Sidebars**: Introduce formal notations as translations of the code, with explicit pronunciation and "how to read out loud" guides.
5. **Bridge to Machine Learning & Modern Autonomy**: Explicitly demonstrate how the concept is used in modern deep learning (LLMs, Diffusion Models, Transformer Attention, Vision Classifiers) and robotic autonomy.
6. **Interactive Companion Demos**: Clean, focused HTML5/Canvas visualizers with dark/light mode toggle.
7. **Comprehensive Sourcing**: Utilize high-quality first-principles explanations, established robotics/ML industry standards, and best practices across the domain.

## The 7 Axon Tracks

1. **`docs/math/`**: Mathematical Foundations (Geometry, Trigonometry, Linear Algebra, Calculus, Probability)
2. **`docs/machine_learning/`**: Core Deep Learning & Computer Vision
3. **`docs/large_language_models/`**: Transformers & Generative AI
4. **`docs/physics/`**: Electromechanics, Dynamics, Projectile Ballistics & Trajectories
5. **`docs/kinematics/`**: Chassis Speeds, Swerve & 2nd-Order Twist, Motion Profiling
6. **`docs/localization/`**: Wheel Odometry, AprilTag Vision PnP, Extended Kalman Filter (EKF)
7. **`docs/reinforcement_learning/`**: MDPs, Q-Learning, Policy Gradients, Monte Carlo Tree Search
