#!/usr/bin/node
module.exports.callMeMoby = function (x, funct) {
  for (let i = 0; i < Number(x); i++) {
    funct();
  }
};
