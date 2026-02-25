import random
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

GATES = ["X", "H", "Z"]
STATES = ["0", "1", "+", "-"]

def prepare_initial_state(qc, state):
    if state == "1":
        qc.x(0)
    elif state == "+":
        qc.h(0)
    elif state == "-":
        qc.x(0)
        qc.h(0)

def apply_gate(qc, gate, player=""):
    qc_name = "Player" if player == "Player" else "Computer"
    print(f"{qc_name} applies: {gate}")
    if gate == "X":
        qc.x(0)
    elif gate == "H":
        qc.h(0)
    elif gate == "Z":
        qc.z(0)

def get_player_gate():
    while True:
        g = input("Choose your gate (X / H / Z): ").upper()
        if g in GATES:
            return g
        else:
            print("Invalid gate. Choose X, H, or Z")

def get_initial_state():
    print("Choose initial qubit state:")
    print("0  → |0⟩")
    print("1  → |1⟩")
    print("+  → |+⟩")
    print("-  → |−⟩")

    while True:
        s = input("Your choice (0 / 1 / + / -): ")
        if s in STATES:
            return s
        else:
            print("Invalid choice")

def main():
    qc = QuantumCircuit(1, 1)

    print("\n🎮 Quantum Strategy Game — Player vs Computer 🤖\n")

    init_state = get_initial_state()
    prepare_initial_state(qc, init_state)

    print(f"\nInitial qubit prepared as |{init_state}⟩\n")

    rounds = 3

    for r in range(rounds):
        print(f"--- Round {r+1} ---")

        player_gate = get_player_gate()
        apply_gate(qc, player_gate, "Player")

        comp_gate = random.choice(GATES)
        apply_gate(qc, comp_gate, "Computer")

        print()

    # Probability calculation
    state = Statevector.from_instruction(qc)
    p0 = abs(state[0])**2
    p1 = abs(state[1])**2

    print("📊 Final Probabilities:")
    print(f"P(|0⟩) = {p0:.4f}")
    print(f"P(|1⟩) = {p1:.4f}\n")

    if abs(p0 - p1) < 1e-6:
        print("🤝 RESULT: DRAW")
    elif p1 > p0:
        print("🔥 RESULT: YOU WIN")
    else:
        print("❄ RESULT: COMPUTER WINS")

    qc.measure(0, 0)

    print("\nFinal Quantum Circuit:\n")
    print(qc)

if __name__ == "__main__":
    main()
