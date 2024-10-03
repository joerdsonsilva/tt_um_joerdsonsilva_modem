/* Generated by Yosys 0.36+42 (git sha1 70d35314d, clang 11.0.1-2 -fPIC -Os) */

module mult3(reset, clk, a0, a1, mult_out);

  wire [6:0] _0_;
  reg [6:0] _1_;
  input [6:0] a0;
  wire [6:0] a0;
  input [6:0] a1;
  wire [6:0] a1;
  input clk;
  wire clk;
  output [6:0] mult_out;
  wire [6:0] mult_out;
  input reset;
  wire reset;
  assign _0_ = a0 ~^ a1;

  always @(posedge clk, posedge reset)
    if (reset) _1_ <= 7'h00;
    else _1_ <= _0_;
  assign mult_out = _1_;
endmodule
