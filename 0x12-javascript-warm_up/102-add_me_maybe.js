#!/usr/bin/env node
module.exports.addMeMaybe = function (x, funct) {
  x = Number(x) + 1;
  funct();
};
