from pydub.generators import Sine

# Define frequencies for each button (C4, E4, G4, A4 for example)
frequencies = [261.63, 329.63, 392.00, 440.00]  # Hz

# Generate tones with an organ-like envelope
tones = [Sine(freq).to_audio_segment(duration=500).fade_in(100).fade_out(100) for freq in frequencies]

# Export or play the tones
for i, tone in enumerate(tones):
    tone.export(f"tone_{i+1}.wav", format="wav")