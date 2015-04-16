import _ from 'lodash';

function hex(value) {
  var str = value.toString(16).toUpperCase();

  if (str.length < 2) {
    str = '0' + str;
  }

  return `(0x${str})`;
}

export default {
  type: 'escape',

  _render() {
    return this.renderLabel(this.label)
      .then(label => {
        label.select('rect').attr({
          rx: 3,
          ry: 3
        });
        return label;
      });
  },

  setup() {
    var addHex;

    this.code = this.properties.esc.properties.code.textValue;
    this.arg = this.properties.esc.properties.arg.textValue;
    [this.label, this.ordinal, addHex] = _.result(this, this.code);

    if (addHex) {
      this.label = `${this.label} ${hex(this.ordinal)}`;
    }
  },

  // Escape code mappings
  b: ['word boundary', -1, false],
  B: ['non-word boundary', -1, false],
  d: ['digit', -1, false],
  D: ['non-digit', -1, false],
  f: ['form feed', 0x0c, true],
  n: ['line feed', 0x0a, true],
  r: ['carriage return', 0x0d, true],
  s: ['white space', -1, false],
  S: ['non-white space', -1, false],
  t: ['tab', 0x09, true],
  v: ['vertical tab', 0x0b, true],
  w: ['word', -1, false],
  W: ['non-word', -1, false],
  1: ['Back reference (group = 1)', -1, false],
  2: ['Back reference (group = 2)', -1, false],
  3: ['Back reference (group = 3)', -1, false],
  4: ['Back reference (group = 4)', -1, false],
  5: ['Back reference (group = 5)', -1, false],
  6: ['Back reference (group = 6)', -1, false],
  7: ['Back reference (group = 7)', -1, false],
  8: ['Back reference (group = 8)', -1, false],
  9: ['Back reference (group = 9)', -1, false],
  0() {
    if (this.arg) {
      return [`octal: ${this.arg}`, parseInt(this.arg, 8), true];
    } else {
      return ['null', 0, true];
    }
  },
  c() {
    return [`ctrl-${this.arg.toUpperCase()}`, this.arg.toUpperCase().charCodeAt(0) - 64, true];
  },
  x() {
    return [`0x${this.arg.toUpperCase()}`, parseInt(this.arg, 16), false];
  },
  u() {
    return [`U+${this.arg.toUpperCase()}`, parseInt(this.arg, 16), false];
  }
};
