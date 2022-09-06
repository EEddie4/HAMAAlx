#!/usr/bin/node

let Base;

function f (nb) {
  return (nb.toString(Base));
}
exports.converter = function (base) {
  Base = base;
  return (f);
};
