# -*- coding: utf-8 -*-
"""
tensorflow_001.py -- TensorFlow Core tutorial
Created on Wed May 10 09:59:26 2017

@author: III
"""
#----------------------------------------------------------------
#Importing TensorFlow
import tensorflow as tf #import tensorflow as tf

#----------------------------------------------------------------
#The Computational Graph
#You might think of TensorFlow Core programs as consisting of two discrete sections:
# 1.Building the computational graph.
# 2.Running the computational graph.
#A computational graph is a series of TensorFlow operations 
#arranged into a graph of nodes.

#TensorFlow operations: 

#----------------------------------------------------------------
#build a simple computational graph
node1=tf.constant(3.0, tf.float32) #floating point Tensors node1
node2=tf.constant(4.0) #floating point Tensors node2
print(node1,node2) #Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)

#printing the nodes does not output the values 3.0 and 4.0
#To actually evaluate the nodes, we must run the computational graph within a session.

#creates a Session object and then invokes its run method to run enough of 
#the computational graph to evaluate node1 and node2.
session01=tf.Session() #creates a Session object
print(session01.run([node1,node2])) #run enough of the computational graph to evaluate node1 and node2.

#------------------------------------------------------------------
#build more complicated computations by combining Tensor nodes with operations (Operations are also nodes.)                
node3=tf.add(node1,node2)
print("node3: ",node3) #node3:  Tensor("Add:0", shape=(), dtype=float32)
                       #尚未運算
print("session01.run(node3): ",session01.run(node3)) #session01.run(node3):  7.0

#TensorBoard

#-------------------------------------------------------
#placeholder
#A placeholder is a promise to provide a value later.
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)
adder_node=a+b # + provides a shortcut for tf.add(a, b)

#evaluate this graph with multiple inputs by using the feed_dict parameter
print(session01.run(adder_node, {a:3,b:4.5})) #7.5

print(session01.run(adder_node, {a:[1,3], b:[2,4]})) #[ 3.  7.]
     #feed_dict parameter 是陣列,就變成陣列相加

#-----------------------------------------------------------
#make the computational graph more complex by adding another operation     
add_and_triple=adder_node*3.0

#evaluate this graph with multiple inputs by using the feed_dict parameter
print(session01.run(add_and_triple, {a:3,b:4.5})) #22.5
print(session01.run(add_and_triple,{a:[1,3],b:[2,4]}))  #[  9.  21.]

#------------------------------------------------------------
#Variables allow us to add trainable parameters to a graph.
#They are constructed with a type and initial value:
w=tf.Variable([.3],tf.float32)
b=tf.Variable([-.3],tf.float32)

x=tf.placeholder(tf.float32)

linear_model=w*x+b

#-------------------------------------------------------------------
#Constants: are initialized when you call tf.constant
#To initialize all the variables in a TensorFlow program, 
#you must explicitly call a special operation as follows:
init=tf.global_variables_initializer()
session01.run(init)  

#Since x is a placeholder, we can evaluate linear_model for several values
# of x simultaneously as follows:
print(session01.run(linear_model,{x:[1,2,3,4]})) #[ 0.          0.30000001  0.60000002  0.90000004]

#--------------------------------------------------------------------
#loss function:
#A loss function measures how far apart the current model is from the provided data.
y = tf.placeholder(tf.float32) #placeholder y
squared_deltas = tf.square(linear_model - y) 
loss = tf.reduce_sum(squared_deltas)
print(session01.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]})) #23.66

#--------------------------------------------------------------------------
#tf.reduce_sum()
# 'x' is [[1, 1, 1]
#         [1, 1, 1]]
#tf.reduce_sum(x) ==> 6
#tf.reduce_sum(x, 0) ==> [2, 2, 2]
#tf.reduce_sum(x, 1) ==> [3, 3]
#tf.reduce_sum(x, 1, keep_dims=True) ==> [[3], [3]]
#tf.reduce_sum(x, [0, 1]) ==> 6










    

