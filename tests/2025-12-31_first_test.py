import patterns.drums as drums
import importlib
importlib.reload(drums)

d1 = Player("d1")
drums.basic_drums(d1)

# --- tempo global ---
Clock.bpm = 140

# --- percussions simples ---
p1 >> play("x-", dur=1/2, mix=0.3)   # kick et snare

# --- basse simple ---
b1 >> bass([0, 1, 3,[1,10]], dur=1, lpf=100)

# --- mélodie légère ---
p2 >> pluck([0, 4, 7, 12], dur=1/4, amp=0.5)

# --- effets en live ---
p1.room = 0.5
p1.mix = 0.3
b1.delay = 0.25
p1.reverb = 0.2

# --- print ---
print(Player.get_attributes())


