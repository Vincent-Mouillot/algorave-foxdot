# --- tempo global ---
Clock.bpm = 140

# --- percussions simples ---
p1 >> play("x-oo-x--[x,o]", dur=1/2)   # kick et snare

# --- basse simple ---
b1 >> bass([0, 1, 3, 5], dur=1, lpf=600)

# --- mélodie légère ---
p2 >> pluck([0, 4, 7, 12], dur=1/4, amp=0.5)

# --- effets en live ---
p1.room = 0.5
p1.mix = 0.3
b1.delay = 0.25
p2.reverb = 0.2
p1.stop()
p2.stop()
b1.stop()
