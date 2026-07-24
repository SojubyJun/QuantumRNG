
#basic bb84 protocol with interception
# @title
import warnings
warnings.filterwarnings('ignore')


try:
    import cirq
except ImportError:
    print('installing cirq...')
    !pip install cirq --quiet
    import cirq
    print('installed cirq.')

my_protocol = BB84(eve_intercept = 'yes')


# Qubit and Simulator
#==================
my_protocol.qubit = cirq.NamedQubit('q0')
my_protocol.simulator = cirq.Simulator()


# Alice's Circuits
#==================
# 0 with no H
circuit = cirq.Circuit()

circuit.append(cirq.I(my_protocol.qubit))
circuit.append(cirq.I(my_protocol.qubit))

my_protocol.alice_send_0_no_H_circuit = circuit


# 1 with no H
circuit = cirq.Circuit()

circuit.append(cirq.X(my_protocol.qubit))
circuit.append(cirq.I(my_protocol.qubit))

my_protocol.alice_send_1_no_H_circuit = circuit


# 0 with H
circuit = cirq.Circuit()

circuit.append(cirq.I(my_protocol.qubit))
circuit.append(cirq.H(my_protocol.qubit))

my_protocol.alice_send_0_H_circuit = circuit


# 1 with H
circuit = cirq.Circuit()

circuit.append(cirq.X(my_protocol.qubit))
circuit.append(cirq.H(my_protocol.qubit))

my_protocol.alice_send_1_H_circuit = circuit


# Bob's Circuits
#==================
# with no H
circuit = cirq.Circuit()

circuit.append(cirq.I(my_protocol.qubit))
circuit.append(cirq.measure(my_protocol.qubit))

my_protocol.bob_receive_no_H_circuit = circuit

# with H
circuit = cirq.Circuit()

circuit.append(cirq.H(my_protocol.qubit))
circuit.append(cirq.measure(my_protocol.qubit))

my_protocol.bob_receive_H_circuit = circuit

