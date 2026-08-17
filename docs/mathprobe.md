# Math rendering probe

Temporary page. Determines how kramdown on GitHub Pages emits math so the
renderer can be wired to the right output. Deleted once answered.

Inline dollar: $a^2 + b^2 = c^2$ end.

Inline paren: \(x_{i+1} = x_i + v\) end.

Display double-dollar:

$$
PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right)
$$

Display bracket:

\[
\gamma(x) = [\sin(2^0 \pi x), \cos(2^0 \pi x), \ldots, \sin(2^{L-1} \pi x)]
\]

Code fence must stay untouched:

```
   PE(pos, 2i) = sin( pos / 10000^(2i/d) )
```

End of probe.
