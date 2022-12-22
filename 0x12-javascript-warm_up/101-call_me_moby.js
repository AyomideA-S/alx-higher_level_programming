#!/usr/bin/node
function callMeMoby (x, theFunction) {
  while (x--) {
    theFunction();
  }
}

exports.callMeMoby = callMeMoby;
