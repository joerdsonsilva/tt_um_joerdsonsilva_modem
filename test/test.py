# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, RisingEdge, FallingEdge, Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 200, units="ns")
    cocotb.start_soon(clock.start())

  # reset
    dut._log.info("reset")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 500)
    await Timer(200, units="ns")

    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1200)

    dut.ui_in <= 0b00
    await ClockCycles(dut.clk, 500)

    dut.ui_in <= 0b01
    await ClockCycles(dut.clk, 2100)

    dut.ui_in <= 0b10
    await ClockCycles(dut.clk, 2100)

    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 500)

    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 300)

    dut.ui_in <= 0b11
    await ClockCycles(dut.clk, 2000)

    dut.ui_in <= 0b00
    await ClockCycles(dut.clk, 500)
