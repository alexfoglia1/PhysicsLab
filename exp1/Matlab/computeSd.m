function [sd] = computeSd (v)
  m = mean(v);
  n = length(v);
  sd = 0;
  for i = 1:n
    sd = sd + (v(i)-m)^2;
  endfor
  sd = sqrt(sd/(n-1));
endfunction