from qiskit import QuantumCircuit, QuantumRegister
import math
from qiskit.quantum_info import Statevector
from qiskit.circuit import Qubit


def inputData():
    N = int(input('Введите N: '))

    q = QuantumRegister(N, name='q')
    bits = []
    
    print('Input bits (1 - True/ skip - False)')
    for i in range(N):
        bits.append(bool(input()))

    return q, bits


def task3_1(q_b, bits_b):
    global circuit
    circuit.h(0)
    circuit.barrier()
    for i in range(1, len(bits_b)):
        if bits_b[i]:
            circuit.cx(q_b[0], q_b[i])


def inputData3_2():
    N = int(input('Введите N: '))
    # 1
    ghz = [1 / math.sqrt(2)]
    for i in range(1, 2 ** N - 1):
        ghz.append(0)
    ghz.append(1 / math.sqrt(2))
    ghz = Statevector(ghz)

    # 2
    w = [0]
    for i in range(1, 2 ** N):
        if i & i - 1:
            w.append(0)
        else:
            w.append(1 / math.sqrt(N))
    w = Statevector(w)

    return ghz, w


def task3_2(q):
    str = q.measure()[0]
    if (len(str) == 1):
        if q == One:
            return 1
        else:
            return 0

    i = 0
    for qubit in str:
        if qubit == '1':
            i += 1
    if (i == 1):
        return 1
    else:
        return 0


def task3_3(q):
    global circuit
    circuit.initialize(q)
    circuit.h(range(2))

    state = Statevector(circuit)
    res = state.measure()[0]
    if res[0] == '0':
        if res[1] == '0':
            return 1
        else:
            return 2
    else:
        if res[1] == '0':
            return 3
        else:
            return 4


S_1 = Statevector([1 / 2, 1 / 2, 1 / 2, 1 / 2])
S_2 = Statevector([1 / 2, -1 / 2, 1 / 2, -1 / 2])
S_3 = Statevector([1 / 2, 1 / 2, -1 / 2, -1 / 2])
S_4 = Statevector([1 / 2, -1 / 2, -1 / 2, 1 / 2])

circuit = QuantumCircuit(2)

print(task3_3(S_2))
