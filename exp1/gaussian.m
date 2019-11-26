function [x,y] = gaussian (h, mu, sigma)
  len = (8*sigma) / h;
  x = linspace(mu-4*sigma, mu+4*sigma, len);
  y = zeros(1, len);
  for i=1:len
    y(i) = 1/sqrt(2*pi*sigma^2) * exp( -0.5*((x(i)-mu)/sigma)^2);
  endfor
endfunction
