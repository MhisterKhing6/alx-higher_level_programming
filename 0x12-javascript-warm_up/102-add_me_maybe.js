#!/usr/bin/node
module.exports.addMeMaybe = function (x, funct) {
  x = Number(x) + 1;
  funct();
};
