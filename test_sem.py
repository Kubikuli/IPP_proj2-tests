from tests.utils_tests import run_sem_test

# Base skeleton for sem testcase
# def test_(tmp_path):
# # 
#     input_text = """

# """.lstrip()

#     expected_codes = {}

#     # Optional user input file (can be empty or contain user input)
#     input_file = tmp_path / "input.txt"
#     input_file.write_text("")  # Empty for this test

#     run_sem_test(str(input_file), input_text, expected_codes)



def test_missing_run(tmp_path):
# class Main : Object {
#     run:
#     [|
#     x := 'hola'.
#     _ := x print.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run:">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="String" value="hola"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {31, 42, 51, 52}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)

def test_missing_main(tmp_path):
# class Ma : Object {
#     run
#     [ | ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Ma" parent="Object">
        <method selector="run">
            <block arity="0"/>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {31, 42, 52}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


def test_unknown_attribute(tmp_path):
# class Main : Object {
#     run
#     [ |
#         _ := self attr: 5.
#         _ := self att.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="attr:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="att">
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {51}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


def test_unknown_variable(tmp_path):
# class Main : Object {
#     run
#     [ |
#     _ := x.
#     _ := (x asString) print.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <var name="x"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {32, 52}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


def test_unknown_variable2(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := 3.
#         y := [| ret := x greaterThan: 0. ] whileTrue:
#         [| r := (x asString) print.
#         x := x minus: 1.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="3"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="whileTrue:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="r"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <send selector="asString">
                                                            <expr>
                                                                <var name="x"/>
                                                            </expr>
                                                        </send>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                        <assign order="2">
                                            <var name="x"/>
                                            <expr>
                                                <send selector="minus:">
                                                    <arg order="1">
                                                        <expr>
                                                            <literal class="Integer" value="1"/>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <var name="x"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <block arity="0">
                                    <assign order="1">
                                        <var name="ret"/>
                                        <expr>
                                            <send selector="greaterThan:">
                                                <arg order="1">
                                                    <expr>
                                                        <literal class="Integer" value="0"/>
                                                    </expr>
                                                </arg>
                                                <expr>
                                                    <var name="x"/>
                                                </expr>
                                            </send>
                                        </expr>
                                    </assign>
                                </block>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {32, 52}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)



def test_DNU_message1(tmp_path):
# class Main : Object {
#     run
#     [ |
#     x := 5.
#     _ := x print.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="5"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {51}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


def test_DNU_message2(tmp_path):
# class Main : Object {
#     run
#     [ |
#     x := 5.
#     _ := x ahoj: 5 jaksemas: 5.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="5"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="ahoj:jaksemas:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="5"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {51}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


def test_DNU_message3(tmp_path):
# class Main : Object {
#     run [|
#         _ := 1 print.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <literal class="Integer" value="1"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {51}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)



def test_DNU_class_method(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := Integer read.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="read">
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {32, 51}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


def test_wrong_from_class(tmp_path):
# class Main : Object {
#     run
#     [ | 
#         x := Integer from: 'ahoj'.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="ahoj"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {53}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)



def test_zero_division(tmp_path):
# class Main: Object{
#     run [|
#         c := Integer from: 5.
#         c := c divBy: 0.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="c"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="c"/>
                    <expr>
                        <send selector="divBy:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="0"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="c"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {53}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


def test_wrong_argument_value(tmp_path):
# class Main : Object {
#     run [|
#         x := Integer from: 3.
#         y := String from: 'ahoj'.

#         x := x plus: y.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="3"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="ahoj"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="String"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="x"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <var name="y"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {53}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


def test_wrong_argument_value2(tmp_path):
# class Main : Object {
#     run [|
#         x := Integer from: 3.
#         y := String from: '2'.

#         x := x plus: y.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="3"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="2"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="String"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="x"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <var name="y"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {53}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


def test_wrong_block_value_msg(tmp_path):
# class Main : Object {
# run [|
#         a := [ :x:y:z |
#                 u := x plus: y.
#                 u := u plus: z. 
#         ].

#         b := a value: 13 value: 42.
#         _ := (b asString) print.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="a"/>
                    <expr>
                        <block arity="3">
                            <parameter order="1" name="x"/>
                            <parameter order="2" name="y"/>
                            <parameter order="3" name="z"/>
                            <assign order="1">
                                <var name="u"/>
                                <expr>
                                    <send selector="plus:">
                                        <arg order="1">
                                            <expr>
                                                <var name="y"/>
                                            </expr>
                                        </arg>
                                        <expr>
                                            <var name="x"/>
                                        </expr>
                                    </send>
                                </expr>
                            </assign>
                            <assign order="2">
                                <var name="u"/>
                                <expr>
                                    <send selector="plus:">
                                        <arg order="1">
                                            <expr>
                                                <var name="z"/>
                                            </expr>
                                        </arg>
                                        <expr>
                                            <var name="u"/>
                                        </expr>
                                    </send>
                                </expr>
                            </assign>
                        </block>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="b"/>
                    <expr>
                        <send selector="value:value:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="13"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="42"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="a"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="b"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {51}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


def test_wrong_block_value_msg2(tmp_path):
# class Main : Object {
# run [|
#         a := [ :x:y |
#                 u := x plus: y. 
#         ].

#         b := a value: 13 value: 42 value: 5.
#         _ := (b asString) print.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="a"/>
                    <expr>
                        <block arity="2">
                            <parameter order="1" name="x"/>
                            <parameter order="2" name="y"/>
                            <assign order="1">
                                <var name="u"/>
                                <expr>
                                    <send selector="plus:">
                                        <arg order="1">
                                            <expr>
                                                <var name="y"/>
                                            </expr>
                                        </arg>
                                        <expr>
                                            <var name="x"/>
                                        </expr>
                                    </send>
                                </expr>
                            </assign>
                        </block>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="b"/>
                    <expr>
                        <send selector="value:value:value:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="13"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="42"/>
                                </expr>
                            </arg>
                            <arg order="3">
                                <expr>
                                    <literal class="Integer" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="a"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="b"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_codes = {51}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)


# ************************ LeO tests ***********************

def test_leo_error_dnu(tmp_path):
# class Main : Object {
#   run [ |
#     _ := self ahoj.
#   ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="_" />
          <expr>
            <send selector="ahoj">
              <expr>
                <var name="self" />
              </expr>
            </send>
          </expr>
        </assign>
      </block>
    </method>
  </class>
</program>
""".lstrip()

    expected_codes = {51}

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_codes)
