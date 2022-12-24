#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  let j = list.length - 1;
  while (i < j) {
    let tmp = list[i];
    list[i++] = list[j];
    list[j--] = tmp;
  }
  return list;
};
