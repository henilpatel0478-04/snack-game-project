# 🐍 Snack Attack! - Arcade Snake Game in Python

An arcade-style Snake & Snack feast game built in Python using **Pygame-CE**. Featuring vibrant procedural food graphics, juicy animations, procedural 8-bit sound effects (zero external audio files needed!), particle explosions, powerups, screen shake, and high score tracking!

---

## 🎮 How to Play

### Run the Game:
```bash
python main.py
```

### Controls:
| Key | Action |
| :--- | :--- |
| **Arrow Keys** or **W, A, S, D** | Move Snake (Up, Down, Left, Right) |
| **SPACE** or **ENTER** | Start Game / Play Again |
| **P** or **SPACE** | Pause / Resume |
| **R** | Quick Restart round |
| **D** | Cycle Difficulty (*Easy*, *Normal*, *Hard*, *Insane*) |
| **W** | Toggle Wall Mode (*Solid Walls* or *Wrap-Around*) |
| **M** | Toggle Sound (Mute / Unmute) |
| **ESC** | Return to Menu / Exit |

---

## 🍕 Snack Menu & Powerups

| Snack | Name | Points | Effect |
| :---: | :--- | :---: | :--- |
| 🍎 | **Crispy Apple** | +10 Pts | Standard growth (+1 segment) |
| 🍕 | **Pizza Slice** | +25 Pts | Savory snack (+2 segments) |
| 🍩 | **Glazed Donut** | +35 Pts | Sweet treat with colorful sprinkles (+2 segments) |
| 🌮 | **Crispy Taco** | +40 Pts | Crunchy bite with spicy fillings (+2 segments) |
| 🍔 | **Cheeseburger** | +50 Pts | Hearty chomp (+3 segments) |
| 🌶️ | **Hot Chili** | +30 Pts | **FRENZY MODE!** 2X points multiplier & rainbow aura for 8s! |
| 🍦 | **Golden Sundae** | +100 Pts | **MEGA BONUS!** Rare timed snack with gold sparkle bursts! |

---

## ✨ Features

- **Expressive Snake**: Cartoon eyes that look in the slithering direction, animated flickering tongue, and smooth gradient-shaded body.
- **Synthesized 8-Bit Retro Audio**: Procedurally generated using Python's standard library `math` and `struct`—crisp munch sounds, powerup sweeps, victory fanfare, and crash thuds without needing external `.wav` files.
- **Dynamic Particle System**: Food crumb explosions with custom colors, floating score popup numbers, and fire trails during frenzy mode.
- **Screen Shake & Game Feel**: Satisfying visual impact upon crashing into walls or self.
- **Customizable Modes**:
  - 4 Difficulty Speeds: Chill (8 steps/s), Classic (12 steps/s), Speedy (16 steps/s), Frenzy (21 steps/s).
  - Wrap-Around (Pac-Man style) vs Solid Walls (Classic retro challenge).
- **Persistent High Scores**: High scores are automatically saved to `highscore.json`.

---

## 🛠️ Requirements

- Python 3.9+ (Fully compatible with Python 3.14+)
- `pygame-ce>=2.5.0` (`pip install pygame-ce`)
