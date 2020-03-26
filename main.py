%matplotlib inline
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()


from qiskit import QuantumRegister,ClassicalRegister
import numpy as np
import math as m


qasm_backend = Aer.backends('qasm_simulator')[0]
vec_backend = Aer.backends('statevector_simulator')[0]

num_bit = int(input('Enter the number of bits - '))

#defining our black box

def black_box(c,fun,num):
    if fun == 'balanced':
        for i in range(num):
            c.cx(q[i],q[num])
        return c
    if fun == 'constant':
        return c
    
    print('{} is not available'.format(fun))
    return 0

q = QuantumRegister(num_bit+1)
c = ClassicalRegister(num_bit)

circuit = QuantumCircuit(q,c)

circuit.x(q[num_bit])
circuit.barrier()

#hadamard from left
for i in range(num_bit+1):
    circuit.h(q[i])
circuit.barrier()

#black_box
circuit = black_box(circuit,'balanced',num_bit)
circuit.barrier()

#hadamard from right
for i in range(num_bit):
    circuit.h(q[i])
circuit.barrier()

#measurement
for i in range(num_bit):
    circuit.measure(q[i],c[i])

#final_job
job = execute(circuit,qasm_backend,shots=1000)
result = job.result()
count = result.get_counts()

plot_histogram(count,legend=['counts'])

#circuit.draw()






