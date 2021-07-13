# Rienforcement Learning to develop AI agents
### Mentors:
- [Adit Khokhar](https://github.com/adit-khokar)
- [Ayush](https://github.com/Ayush-Ranjan)

 This project "Learning RL to develop AI agents" is offered by ACA(Association of Computer Activities IITK).
 ## General Concepts :
 ### <u> Introduction to Machine Learning </u>
 Field of study that gives computers the ability to learn without being explicitly programmed.<br>
 A computer program is said to learn from experience E with respect to some task T and some performance measure P,if its performance on T,as measured by P, improves with experience E.
 #### <ins>Machine learning algorithms:</ins>
- Supervised learning
- Unsupervised learning
- ***Reinforcement learning.*** 

#### <ins>Model Representation</ins>
Generaling speaking,The aim of the supervised learning algorithm is to use the given training Dataset and output a ***Hypothesis function***.Where Hypothesis function takes the input instance and predicts the output based on its learnings from the training dataset.
![alt text](https://machinelearningmedium.com/assets/2017-08-10-model-representation-and-hypothesis/fig-1-hypothesis.png?raw=true)

##### <ins>Linear	regression	with	one	variable.</ins>

For linear regression in one variable,the hypothesis function will be of the form-<br>
h(x) = ***Θ***0 + ***Θ***1*x         <br>where, ***Θ***0 and ***Θ***1 are the parameters.


![alt text](https://miro.medium.com/max/337/1*6egMs9kaw3HFwtQiANtoaQ.png?raw=true)

The line seen in the graph is the Hypothesis function. This line is the best fit that passes through most of the points.<br>
Now we know it's not possible to tell the hypothesis function by merely looking at the graph! We need some systematic way to figure it out.<br>

<ins>***Cost Function***</ins> helps us to figure out which hypothesis best fits our data. Or more formally,It helps us to measure the <ins>error</ins> of our hypothesis.It's often called the squared error function.<br><br>
Mathematically, Cost function —<br>
![alt text](https://miro.medium.com/max/431/1*xXr2YaMcE0KnFAimpT2kHA.png?raw=true)

<pre>
(h(x) — y)² : Squared vertical distances of the scattered points from the hypothesis.
∑(h(x) — y)²/2m: Average Squared vertical distances of the scattered points from the hypothesis, i.e Mean Squared error.
</pre>

Now we have our hypothesis function and we also have a method of measuring how well it fits into the given data.All we need to do is find the value of parameters(***Θ***0 and ***Θ***1) for which the cost function (i.e. error) is minimum.<br> That’s where gradient descent comes into the picture

<ins>***Gradient descent***</ins> is an optimization algorithm for finding a local minimum of a differentiable function.Gradient descent is simply used to find the values of a function's parameters that minimize a cost function as much as possible.[Here](https://builtin.com/data-science/gradient-descent) you can find more details about Gradient descent.<br>
![alt text](https://miro.medium.com/max/600/0*OHYVpB111n4tr80y?raw=true)

Mathematical form of Gradient Descent for Linear Regression-<br>

repeat until Convergence:{
                   \Theta(0) := \Theta(0) - (alpha/m)*  $\sum\limits_{i=0}^m (h(xi)-yi)
(
\Theta
