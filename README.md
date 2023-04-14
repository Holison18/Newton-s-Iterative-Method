# Newton-s-Iterative-Method
Newton's Non Linear iterative Method is a method that helps us to find the roots of a non-linear equation by guessing an intial value and performing the 
iterations n number of times.
<h2>Method</h2>
<ul>
  <li>First of all we pick an initial guess,x0</li>
  <li>We use the first order taylor's series expansion at x to find the values of xi</li>
  f(x) = f(x0) + 1/1!*(f'(x0)(x-x))
  making x the subject we get,
  xi = x(i-1) - f(x(i-1))/f'(x(i-1))
  <li>We repeat the producedure until our approximated value is closer enough to our actual value</li>
</ul>
This python program allow the user to find the roots of a non linear equation by inputting the function the derivative of the function, the initial guess
and the number of iterations.
