from tests.utils_tests import run_test

# Base skeleton for testcase
# def test_(tmp_path):
#     input_text = """

# """.lstrip()

#     expected_output = ""

#     # Optional user input file (can be empty or contain user input)
#     input_file = tmp_path / "input.txt"
#     input_file.write_text("")  # Empty for this test

#     run_test(str(input_file), input_text, expected_output)


def test_basic_output(tmp_path):
# class Main : Object {
#     run
#     [|
#     x := 'hola'.
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

    expected_output = "hola"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_basic_int_output(tmp_path):
# class Main : Object {
#     run
#     [|
#     x := 5.
#     y := x asString.
#     _ := y print.
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
                    <var name="y"/>
                    <expr>
                        <send selector="asString">
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "5"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

def test_plus(tmp_path):
# class Main : Object {
#     run
#     [|
#     x := 5.
#     y := x plus: 2.
#     x := y asString.
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
                    <var name="y"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="2"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="x"/>
                    <expr>
                        <send selector="asString">
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
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

    expected_output = "7"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

def test_all_basic_math(tmp_path):
# class Main : Object {
#     run
#     [|
#     x := 5.
#     y := x minus: 2.
#     x := y multiplyBy: 4.
#     y := x divBy: 3.
#     _ := (y asString) print.
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
                    <var name="y"/>
                    <expr>
                        <send selector="minus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="2"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="x"/>
                    <expr>
                        <send selector="multiplyBy:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="4"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="y"/>
                    <expr>
                        <send selector="divBy:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="3"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="y"/>
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

    expected_output = "4"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

def test_read(tmp_path):
# class Main : Object {
#     run
#     [|
#     x := String read.
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
                        <send selector="read">
                            <expr>
                                <literal class="class" value="String"/>
                            </expr>
                        </send>
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

    expected_output = "ahoj"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("ahoj")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

def test_basic_attr_create(tmp_path):
# class Main : Object {
#     run
#     [ |
#         _ := self attr: 5.
#         x := (self attr) plus: 2.
#         _ := (x asString) print.
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
                    <var name="x"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="2"/>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="attr">
                                    <expr>
                                        <var name="self"/>
                                    </expr>
                                </send>
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

    expected_output = "7"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_block_result(tmp_path):
# class Main : Object {
# run [|
#     a := self foo: 4.
#     _ := (a asString) print.
#     b := [ :x | _ := 42. ].
#     c := b value: 16.
#     _ := (c asString) print.
#     d := 'ahoj' print .
#     _ := d print.
# ]
# foo: [ :x |
#     u := x plus: 10.
# ]
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
                        <send selector="foo:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="4"/>
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
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="a"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="b"/>
                    <expr>
                        <block arity="1">
                            <parameter order="1" name="x"/>
                            <assign order="1">
                                <var name="_"/>
                                <expr>
                                    <literal class="Integer" value="42"/>
                                </expr>
                            </assign>
                        </block>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="c"/>
                    <expr>
                        <send selector="value:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="16"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="b"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="c"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="d"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <literal class="String" value="ahoj"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="7">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="d"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
        <method selector="foo:">
            <block arity="1">
                <parameter order="1" name="x"/>
                <assign order="1">
                    <var name="u"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="10"/>
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

    expected_output = "1442ahojahoj"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_block_skip_def(tmp_path):
# class Main : Object {
# run [|
#     a := [ | _ := (8 asString) print. ].
#     c := a value.
#   ]
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
                        <block arity="0">
                            <assign order="1">
                                <var name="_"/>
                                <expr>
                                    <send selector="print">
                                        <expr>
                                            <send selector="asString">
                                                <expr>
                                                    <literal class="Integer" value="8"/>
                                                </expr>
                                            </send>
                                        </expr>
                                    </send>
                                </expr>
                            </assign>
                        </block>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="c"/>
                    <expr>
                        <send selector="value">
                            <expr>
                                <var name="a"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "8"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_method_redefinition(tmp_path):
# class Main : Object {
#     run
#     [|
#         x := MyInt from: 10.
#         y := x multiplyBy: 5.
#         _ := (y asString) print.
#     ]
# }

# class MyInt : Integer {
#     multiplyBy:
#     [ :x| 
#         r := self minus: x.
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
                                    <literal class="Integer" value="10"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="multiplyBy:">
                            <arg order="1">
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
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="y"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="MyInt" parent="Integer">
        <method selector="multiplyBy:">
            <block arity="1">
                <parameter order="1" name="x"/>
                <assign order="1">
                    <var name="r"/>
                    <expr>
                        <send selector="minus:">
                            <arg order="1">
                                <expr>
                                    <var name="x"/>
                                </expr>
                            </arg>
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

    expected_output = "5"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_factorial(tmp_path):
# class Factorial : Integer {
#     factorial
#         [| 
#         r := (self equalTo: 0) ifTrue: [|r := Factorial from: 1.]
#         ifFalse: [|r := self multiplyBy:
#         (( Factorial from:(self plus: -1)) factorial) . ].
#     ]
# }
# class Main : Object {
#     run
#     [| 
#         x := Factorial from: (( String read) asInteger). 
#         x := ((x factorial) asString) print. 
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Factorial" parent="Integer">
        <method selector="factorial">
            <block arity="0">
                <assign order="1">
                    <var name="r"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="r"/>
                                            <expr>
                                                <send selector="from:">
                                                    <arg order="1">
                                                        <expr>
                                                            <literal class="Integer" value="1"/>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <literal class="class" value="Factorial"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="r"/>
                                            <expr>
                                                <send selector="multiplyBy:">
                                                    <arg order="1">
                                                        <expr>
                                                            <send selector="factorial">
                                                                <expr>
                                                                    <send selector="from:">
                                                                        <arg order="1">
                                                                            <expr>
                                                                                <send selector="plus:">
                                                                                    <arg order="1">
                                                                                        <expr>
                                                                                            <literal class="Integer" value="-1"/>
                                                                                        </expr>
                                                                                    </arg>
                                                                                    <expr>
                                                                                        <var name="self"/>
                                                                                    </expr>
                                                                                </send>
                                                                            </expr>
                                                                        </arg>
                                                                        <expr>
                                                                            <literal class="class" value="Factorial"/>
                                                                        </expr>
                                                                    </send>
                                                                </expr>
                                                            </send>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <var name="self"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="equalTo:">
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="0"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="self"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <send selector="asInteger">
                                        <expr>
                                            <send selector="read">
                                                <expr>
                                                    <literal class="class" value="String"/>
                                                </expr>
                                            </send>
                                        </expr>
                                    </send>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Factorial"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="x"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <send selector="factorial">
                                            <expr>
                                                <var name="x"/>
                                            </expr>
                                        </send>
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

    expected_output = "120"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("5")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_if_then(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := 3.
#         _ := (x greaterThan: 0)
#         ifTrue: [|u := 'ANO' print.]
#         ifFalse: [|u := 'NE' print.]. 
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
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
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
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_if_else(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := 3.
#         _ := (x greaterThan: 3)
#         ifTrue: [|u := 'ANO' print.]
#         ifFalse: [|u := 'NE' print.]. 
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
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="greaterThan:">
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="3"/>
                                        </expr>
                                    </arg>
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

    expected_output = "NE"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_reassign(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := 3.
#         x := x plus: 5.
#         _ := (x greaterThan: 5)
#         ifTrue: [|u := 'ANO' print.]
#         ifFalse: [|u := 'NE' print.]. 
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
                    <var name="x"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
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
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="greaterThan:">
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="5"/>
                                        </expr>
                                    </arg>
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

    expected_output = "ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_wrong_assign_order(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := 3.
#         x := x plus: 2.
#         x := x multiplyBy: 4.
#         _ := (x asString) print. 
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="3">
                    <var name="x"/>
                    <expr>
                        <send selector="multiplyBy:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="4"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="3"/>
                    </expr>
                </assign>
                <assign order="4">
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
                <assign order="2">
                    <var name="x"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="2"/>
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

    expected_output = "20"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_wrong_param_order(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := self fo: 9 fo: 3.
#         _ := (x asString) print.
#     ]

#     fo:fo:[:x :y|
#         _ := x divBy: y.
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
                        <send selector="fo:fo:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="9"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="3"/>
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
        <method selector="fo:fo:">
            <block arity="2">
                <parameter order="2" name="y"/>
                <parameter order="1" name="x"/>
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="divBy:">
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

    expected_output = "3"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_wrong_arg_order(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := self fo: 9 fo: 3.
#         _ := (x asString) print.
#     ]

#     fo:fo:[:x :y|
#         _ := x divBy: y.
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
                        <send selector="fo:fo:">
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="3"/>
                                </expr>
                            </arg>
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="9"/>
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
        <method selector="fo:fo:">
            <block arity="2">
                <parameter order="1" name="x"/>
                <parameter order="2" name="y"/>
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="divBy:">
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

    expected_output = "3"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_if_then2(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := MyInt from: 3.
#         x := ((x condition) asString) print.
#     ]
# }

# class MyInt : Integer{
#     condition
#     [|
#         _ := (self greaterThan: 0)
#         ifTrue: [|u := self plus: 2.]
#         ifFalse: [|u := self minus: 2.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25" description="&lt;- definice metody - bezparametrický selektor run">
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
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="x"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <send selector="condition">
                                            <expr>
                                                <var name="x"/>
                                            </expr>
                                        </send>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="MyInt" parent="Integer">
        <method selector="condition">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="plus:">
                                                    <arg order="1">
                                                        <expr>
                                                            <literal class="Integer" value="2"/>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <var name="self"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="minus:">
                                                    <arg order="1">
                                                        <expr>
                                                            <literal class="Integer" value="2"/>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <var name="self"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="greaterThan:">
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="0"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="self"/>
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

    expected_output = "5"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_if_else2(tmp_path):
# class Main : Object {
#     run "<- definice metody - bezparametrický selektor run"
#     [ |
#         x := MyInt from: 3.
#         x := ((x condition) asString) print.
#     ]
# }

# class MyInt : Integer{
#     condition
#     [|
#         _ := (self greaterThan: 5)
#         ifTrue: [|u := self plus: 2.]
#         ifFalse: [|u := self minus: 2.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25" description="&lt;- definice metody - bezparametrický selektor run">
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
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="x"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <send selector="condition">
                                            <expr>
                                                <var name="x"/>
                                            </expr>
                                        </send>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="MyInt" parent="Integer">
        <method selector="condition">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="plus:">
                                                    <arg order="1">
                                                        <expr>
                                                            <literal class="Integer" value="2"/>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <var name="self"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="minus:">
                                                    <arg order="1">
                                                        <expr>
                                                            <literal class="Integer" value="2"/>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <var name="self"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="greaterThan:">
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
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "1"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_whileTrue2(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := self attr: 3.
#         y := [| ret := (self attr) greaterThan: 0. ] whileTrue:
#         [| r := ((self attr) asString) print.
#         r := self attr: ((self attr) minus: 1).].
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
                        <send selector="attr:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="3"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
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
                                                                <send selector="attr">
                                                                    <expr>
                                                                        <var name="self"/>
                                                                    </expr>
                                                                </send>
                                                            </expr>
                                                        </send>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                        <assign order="2">
                                            <var name="r"/>
                                            <expr>
                                                <send selector="attr:">
                                                    <arg order="1">
                                                        <expr>
                                                            <send selector="minus:">
                                                                <arg order="1">
                                                                    <expr>
                                                                        <literal class="Integer" value="1"/>
                                                                    </expr>
                                                                </arg>
                                                                <expr>
                                                                    <send selector="attr">
                                                                        <expr>
                                                                            <var name="self"/>
                                                                        </expr>
                                                                    </send>
                                                                </expr>
                                                            </send>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <var name="self"/>
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
                                                    <send selector="attr">
                                                        <expr>
                                                            <var name="self"/>
                                                        </expr>
                                                    </send>
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

    expected_output = "321"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_timesRepeat(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := 5.
#         y := x timesRepeat:
#         [:i| r := (i asString) print.].
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
                    <var name="y"/>
                    <expr>
                        <send selector="timesRepeat:">
                            <arg order="1">
                                <expr>
                                    <block arity="1">
                                        <parameter order="1" name="i"/>
                                        <assign order="1">
                                            <var name="r"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <send selector="asString">
                                                            <expr>
                                                                <var name="i"/>
                                                            </expr>
                                                        </send>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
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

    expected_output = "12345"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)





def test_block_job(tmp_path):
# class Main : Object {
#     run
#     [|
#         b1 := [ | a := String read. _ := a print. ].
#         b2 := [ :x | _ := x plus: 1. ].
#         b3 := [ :x:y | val := x value: y. ].
#         _ := b1 value.
#         c := b3 value: b2 value: 3.
#         _ := (c asString) print.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="b1"/>
                    <expr>
                        <block arity="0">
                            <assign order="1">
                                <var name="a"/>
                                <expr>
                                    <send selector="read">
                                        <expr>
                                            <literal class="class" value="String"/>
                                        </expr>
                                    </send>
                                </expr>
                            </assign>
                            <assign order="2">
                                <var name="_"/>
                                <expr>
                                    <send selector="print">
                                        <expr>
                                            <var name="a"/>
                                        </expr>
                                    </send>
                                </expr>
                            </assign>
                        </block>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="b2"/>
                    <expr>
                        <block arity="1">
                            <parameter order="1" name="x"/>
                            <assign order="1">
                                <var name="_"/>
                                <expr>
                                    <send selector="plus:">
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
                </assign>
                <assign order="3">
                    <var name="b3"/>
                    <expr>
                        <block arity="2">
                            <parameter order="1" name="x"/>
                            <parameter order="2" name="y"/>
                            <assign order="1">
                                <var name="val"/>
                                <expr>
                                    <send selector="value:">
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
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="value">
                            <expr>
                                <var name="b1"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="c"/>
                    <expr>
                        <send selector="value:value:">
                            <arg order="1">
                                <expr>
                                    <var name="b2"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="3"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="b3"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="c"/>
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

    expected_output = "b4"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("b")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_spec_message_sending(tmp_path):
# class Main : Object {
#     run [|
#         a := self attrib: (Integer from: 10).
#         b := [| x := ((self attrib) asString) concatenateWith: (10 asString). ].
#         _ := (b value) print.
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
                        <send selector="attrib:">
                            <arg order="1">
                                <expr>
                                    <send selector="from:">
                                        <arg order="1">
                                            <expr>
                                                <literal class="Integer" value="10"/>
                                            </expr>
                                        </arg>
                                        <expr>
                                            <literal class="class" value="Integer"/>
                                        </expr>
                                    </send>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="b"/>
                    <expr>
                        <block arity="0">
                            <assign order="1">
                                <var name="x"/>
                                <expr>
                                    <send selector="concatenateWith:">
                                        <arg order="1">
                                            <expr>
                                                <send selector="asString">
                                                    <expr>
                                                        <literal class="Integer" value="10"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </arg>
                                        <expr>
                                            <send selector="asString">
                                                <expr>
                                                    <send selector="attrib">
                                                        <expr>
                                                            <var name="self"/>
                                                        </expr>
                                                    </send>
                                                </expr>
                                            </send>
                                        </expr>
                                    </send>
                                </expr>
                            </assign>
                        </block>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="value">
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

    expected_output = "1010"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_spec_page10(tmp_path):
# class Main : Object {
#     run [|
#         a := A new.
#         b := [ :arg | y := self attr: arg. z := self. ].
#         c := a foo: b.
#         _ := ((c attr) asString) print.
#     ]
# }

# class A : Object {
#         foo: [ :x |
#         u := x value: 1.
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
                        <send selector="new">
                            <expr>
                                <literal class="class" value="A"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="b"/>
                    <expr>
                        <block arity="1">
                            <parameter order="1" name="arg"/>
                            <assign order="1">
                                <var name="y"/>
                                <expr>
                                    <send selector="attr:">
                                        <arg order="1">
                                            <expr>
                                                <var name="arg"/>
                                            </expr>
                                        </arg>
                                        <expr>
                                            <var name="self"/>
                                        </expr>
                                    </send>
                                </expr>
                            </assign>
                            <assign order="2">
                                <var name="z"/>
                                <expr>
                                    <var name="self"/>
                                </expr>
                            </assign>
                        </block>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="c"/>
                    <expr>
                        <send selector="foo:">
                            <arg order="1">
                                <expr>
                                    <var name="b"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="a"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <send selector="attr">
                                            <expr>
                                                <var name="c"/>
                                            </expr>
                                        </send>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="A" parent="Object">
        <method selector="foo:">
            <block arity="1">
                <parameter order="1" name="x"/>
                <assign order="1">
                    <var name="u"/>
                    <expr>
                        <send selector="value:">
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
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "1"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_spec_page12(tmp_path):
# class Main : Object {
#     run [|
#         r := self value: 10.
#         e := self next: (self value).
#         t := self value: nil.
#         _ := ((self value) asString) print.
#         _ := ((self next) asString) print.
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="r"/>
                    <expr>
                        <send selector="value:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="10"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="e"/>
                    <expr>
                        <send selector="next:">
                            <arg order="1">
                                <expr>
                                    <send selector="value">
                                        <expr>
                                            <var name="self"/>
                                        </expr>
                                    </send>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="t"/>
                    <expr>
                        <send selector="value:">
                            <arg order="1">
                                <expr>
                                    <literal class="Nil" value="nil"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <send selector="value">
                                            <expr>
                                                <var name="self"/>
                                            </expr>
                                        </send>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <send selector="next">
                                            <expr>
                                                <var name="self"/>
                                            </expr>
                                        </send>
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

    expected_output = "nil10"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_super(tmp_path):
# class Main : Object {
#     run [|
#         x := MyInt from: 8.
#         x := x foo.
#         _ := (x asString) print.
#     ]
# }

# class MyInt : Integer {
#     foo[|
#         _ := MyInt from: ((super plus: 100) asInteger).
#     ]

# "plus redefined to print given value"
#     plus:[:x|
#         _ := (x asString) print.
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25" description="plus redefined to print given value">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="8"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="x"/>
                    <expr>
                        <send selector="foo">
                            <expr>
                                <var name="x"/>
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
    <class name="MyInt" parent="Integer">
        <method selector="foo">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <send selector="asInteger">
                                        <expr>
                                            <send selector="plus:">
                                                <arg order="1">
                                                    <expr>
                                                        <literal class="Integer" value="100"/>
                                                    </expr>
                                                </arg>
                                                <expr>
                                                    <var name="super"/>
                                                </expr>
                                            </send>
                                        </expr>
                                    </send>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
        <method selector="plus:">
            <block arity="1">
                <parameter order="1" name="x"/>
                <assign order="1">
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

    expected_output = "108"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_attribute_inheritance(tmp_path):
# class A: Integer {}
# class Main: Object{
#   run [|
#       x := A from: ((Integer from: 1) value: (Integer from: 2)).
#       _ := (x asString) print.
#       _ := ((x value) asString) print.
#   ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="A" parent="Integer"/>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <send selector="value:">
                                        <arg order="1">
                                            <expr>
                                                <send selector="from:">
                                                    <arg order="1">
                                                        <expr>
                                                            <literal class="Integer" value="2"/>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <literal class="class" value="Integer"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </arg>
                                        <expr>
                                            <send selector="from:">
                                                <arg order="1">
                                                    <expr>
                                                        <literal class="Integer" value="1"/>
                                                    </expr>
                                                </arg>
                                                <expr>
                                                    <literal class="class" value="Integer"/>
                                                </expr>
                                            </send>
                                        </expr>
                                    </send>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="A"/>
                            </expr>
                        </send>
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
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <send selector="value">
                                            <expr>
                                                <var name="x"/>
                                            </expr>
                                        </send>
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

    expected_output = "12"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_transitive_inheritance1(tmp_path):
# class A: Integer {
#   foo [|
#     _ := 'A foo'.
#   ]
# }
# class B: A {
#     bar [|
#     _ := 'B bar'.
#   ]
# }
# class C: B {
#     baz [|
#     _ := 'C baz'.
#   ]
# }

# class Main: Object{
#   run [|
#     c := C new.
#     _ := (c foo) print.
#     _ := (c bar) print.
#     _ := (c baz) print.

#     c := c plus: 4.
#     _ := (c asString) print.
#   ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="A" parent="Integer">
        <method selector="foo">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <literal class="String" value="A foo"/>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="B" parent="A">
        <method selector="bar">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <literal class="String" value="B bar"/>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="C" parent="B">
        <method selector="baz">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <literal class="String" value="C baz"/>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="c"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="C"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="foo">
                                    <expr>
                                        <var name="c"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="bar">
                                    <expr>
                                        <var name="c"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="baz">
                                    <expr>
                                        <var name="c"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="c"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="4"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="c"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="c"/>
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

    expected_output = "A fooB barC baz4"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_transitive_inheritance2(tmp_path):
# class B: A {
#     bar [|
#     _ := 'B bar'.
#   ]
# }
# class A: Integer {
#   foo [|
#     _ := 'A foo'.
#   ]
# }
# class C: B {
#     baz [|
#     _ := 'C baz'.
#   ]
# }

# class Main: Object{
#   run [|
#     c := C new.
#     _ := (c foo) print.
#     _ := (c bar) print.
#     _ := (c baz) print.

#     c := c plus: 4.
#     _ := (c asString) print.
#   ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="B" parent="A">
        <method selector="bar">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <literal class="String" value="B bar"/>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="A" parent="Integer">
        <method selector="foo">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <literal class="String" value="A foo"/>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="C" parent="B">
        <method selector="baz">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <literal class="String" value="C baz"/>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="c"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="C"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="foo">
                                    <expr>
                                        <var name="c"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="bar">
                                    <expr>
                                        <var name="c"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="baz">
                                    <expr>
                                        <var name="c"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="c"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="4"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="c"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="c"/>
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

    expected_output = "A fooB barC baz4"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_short_circuit_evaluation(tmp_path):
# class Main : Object {
#     run [|
#         x := True new.
#         y := False new.
#         w := Object new.

#         z := x or: w.
#         u := y and: w.

#         _ := z
#         ifTrue: [| _ := 'ANO ' print.]
#         ifFalse: [| _ := 'NE ' print.].

#         _ := u
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
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
                        <send selector="new">
                            <expr>
                                <literal class="class" value="True"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="False"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="w"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="Object"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="z"/>
                    <expr>
                        <send selector="or:">
                            <arg order="1">
                                <expr>
                                    <var name="w"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="u"/>
                    <expr>
                        <send selector="and:">
                            <arg order="1">
                                <expr>
                                    <var name="w"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <var name="z"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="7">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <var name="u"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ANO NE"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_block_triple_value(tmp_path):
# class Main : Object {
# run [|
#         a := [ :x:y:z |
#                 u := x plus: y.
#                 u := u plus: z. 
#         ].

#         b := a value: 13 value: 42 value: 10.
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
                                    <literal class="Integer" value="10"/>
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

    expected_output = "65"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_example_simplified(tmp_path):
# class Main : Object {
#     run
#     [ |
#         x := self compute: 3 and: 2 and: 5.
#         x := self plusOne: (self vysl).
#         y := x asString .
#         _ := y print.
#     ]
    
#     plusOne: 
#     [ :x | 
#         r := x plus: 1. 
#     ]
    
#     compute:and:and: 
#     [ :x :y :z |
#         a := x plus: y.
#         _ := self vysl: a.
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
                        <send selector="compute:and:and:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="3"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="2"/>
                                </expr>
                            </arg>
                            <arg order="3">
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
                    <var name="x"/>
                    <expr>
                        <send selector="plusOne:">
                            <arg order="1">
                                <expr>
                                    <send selector="vysl">
                                        <expr>
                                            <var name="self"/>
                                        </expr>
                                    </send>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="y"/>
                    <expr>
                        <send selector="asString">
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
        <method selector="plusOne:">
            <block arity="1">
                <parameter order="1" name="x"/>
                <assign order="1">
                    <var name="r"/>
                    <expr>
                        <send selector="plus:">
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
        </method>
        <method selector="compute:and:and:">
            <block arity="3">
                <parameter order="1" name="x"/>
                <parameter order="2" name="y"/>
                <parameter order="3" name="z"/>
                <assign order="1">
                    <var name="a"/>
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
                    <var name="_"/>
                    <expr>
                        <send selector="vysl:">
                            <arg order="1">
                                <expr>
                                    <var name="a"/>
                                </expr>
                            </arg>
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

    expected_output = "6"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_example(tmp_path):
# class Main : Object {
#     run "<- definice metody - bezparametrický selektor run"
#     [ |
#         x := self compute: 3 and: 2 and: 5.
#         x := self plusOne: (self vysl).
#         y := x asString .
#         _ := y print.
#     ]
    
#     plusOne: 
#     [ :x | 
#         r := x plus: 1. 
#     ]
    
#     compute:and:and: 
#     [ :x :y :z |    
#         a := x plus: y.
#         _ := self vysl: a.
#         _ := (( self vysl) greaterThan: 0)
#         ifTrue: [|u := self vysl: 1.]
#         ifFalse: [|].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25" description="&lt;- definice metody - bezparametrický selektor run">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="compute:and:and:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="3"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="2"/>
                                </expr>
                            </arg>
                            <arg order="3">
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
                    <var name="x"/>
                    <expr>
                        <send selector="plusOne:">
                            <arg order="1">
                                <expr>
                                    <send selector="vysl">
                                        <expr>
                                            <var name="self"/>
                                        </expr>
                                    </send>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="y"/>
                    <expr>
                        <send selector="asString">
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
        <method selector="plusOne:">
            <block arity="1">
                <parameter order="1" name="x"/>
                <assign order="1">
                    <var name="r"/>
                    <expr>
                        <send selector="plus:">
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
        </method>
        <method selector="compute:and:and:">
            <block arity="3">
                <parameter order="1" name="x"/>
                <parameter order="2" name="y"/>
                <parameter order="3" name="z"/>
                <assign order="1">
                    <var name="a"/>
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
                    <var name="_"/>
                    <expr>
                        <send selector="vysl:">
                            <arg order="1">
                                <expr>
                                    <var name="a"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="vysl:">
                                                    <arg order="1">
                                                        <expr>
                                                            <literal class="Integer" value="1"/>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <var name="self"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0"/>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="greaterThan:">
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="0"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <send selector="vysl">
                                            <expr>
                                                <var name="self"/>
                                            </expr>
                                        </send>
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

    expected_output = "2"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_escape_seq1(tmp_path):
# class Main : Object {
#   run [|
#     _ := 'Ahoj\nahoj' print.
#   ]
# }

    input_text = r"""
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
                                <literal class="String" value="Ahoj\nahoj"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "Ahoj\nahoj"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_escape_seq2(tmp_path):
# class Main : Object {
#   run [|
#     _ := 'Ahoj\\ahoj' print.
#   ]
# }

    input_text = r"""
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
                                <literal class="String" value="Ahoj\\ahoj"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = r"Ahoj\ahoj"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_escape_seq3(tmp_path):
# class Main : Object {
#   run [|
#     _ := 'Ahoj\'ahoj' print.
#   ]
# }

    input_text = r"""
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
                                <literal class="String" value="Ahoj\'ahoj"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "Ahoj'ahoj"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_escape_seq4(tmp_path):
# class Main : Object {
#   run [|
#     _ := 'Ahoj\n\'Sve"te \\\'' print.
#   ]
# }

    input_text = r"""
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
                                <literal class="String" value="Ahoj\n\'Sve&quot;te \\\'"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "Ahoj\n'Sve\"te \\'"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_nil_singleton(tmp_path):
# class Main : Object {
#   run [ |
#     y := Nil new.
#     x := Nil new.
#     _ := x attr: 5.
#     _ := ((y attr) asString) print.
#   ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="y"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="Nil"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="x"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="Nil"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="attr:">
                            <arg order="1">
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
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <send selector="attr">
                                            <expr>
                                                <var name="y"/>
                                            </expr>
                                        </send>
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

    expected_output = "5"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


# ************************** TESTS BY @alklk *****************************
 
def test_ifTrue_ifFalse(tmp_path):
# class TrueBlock : Object {
#   value[|
#     _ := 'value from true\n' print.
#   ]
# }

# class FalseBlock : Object {
#   value[|
#     _ := 'value from false\n' print.
#   ]
# }

# class Main : Object {
#   run [|
#     t := TrueBlock new.
#     f := FalseBlock new.
#     _ := true ifTrue: t ifFalse: f.
#     _ := false ifTrue: t ifFalse: f.
#   ]
# }
    input_text = r"""
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="TrueBlock" parent="Object">
        <method selector="value">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <literal class="String" value="value from true\n"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="FalseBlock" parent="Object">
        <method selector="value">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <literal class="String" value="value from false\n"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="t"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="TrueBlock"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="f"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="FalseBlock"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <var name="t"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <var name="f"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="True" value="true"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <var name="t"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <var name="f"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="False" value="false"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "value from true\nvalue from false\n"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_whileTrue(tmp_path):
# class WhileTrueBlockBase : Block {
#   init[|
#     ret := self i: 5.
#   ]

#   value [|
#     _ := self i: ((self i) minus: 1).
#     ret := (self i) greaterThan: 0.
#   ]
# }

# class WhileTrueBlock : Object {
#   value [|
#     ret := 'ahoj' print.
#   ]
# }

# class Main : Object {
#   run [|
#     t := WhileTrueBlock new.
#     b := (WhileTrueBlockBase new) init.
#     y := b whileTrue: t.
#   ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="WhileTrueBlockBase" parent="Block">
        <method selector="init">
            <block arity="0">
                <assign order="1">
                    <var name="ret"/>
                    <expr>
                        <send selector="i:">
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
            </block>
        </method>
        <method selector="value">
            <block arity="0">
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="i:">
                            <arg order="1">
                                <expr>
                                    <send selector="minus:">
                                        <arg order="1">
                                            <expr>
                                                <literal class="Integer" value="1"/>
                                            </expr>
                                        </arg>
                                        <expr>
                                            <send selector="i">
                                                <expr>
                                                    <var name="self"/>
                                                </expr>
                                            </send>
                                        </expr>
                                    </send>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="ret"/>
                    <expr>
                        <send selector="greaterThan:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="0"/>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="i">
                                    <expr>
                                        <var name="self"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="WhileTrueBlock" parent="Object">
        <method selector="value">
            <block arity="0">
                <assign order="1">
                    <var name="ret"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <literal class="String" value="ahoj"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="t"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="WhileTrueBlock"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="b"/>
                    <expr>
                        <send selector="init">
                            <expr>
                                <send selector="new">
                                    <expr>
                                        <literal class="class" value="WhileTrueBlockBase"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="y"/>
                    <expr>
                        <send selector="whileTrue:">
                            <arg order="1">
                                <expr>
                                    <var name="t"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="b"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ahojahojahojahoj"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_timesRepeat2(tmp_path):
# class TimesRepeatBlock : Object {
#   value: [ :arg |
#     _ := (arg asString) print.
#   ]
# }

# class Main : Object {
#   run [|
#     trp := TimesRepeatBlock new.
#     t := 5 timesRepeat: trp. 
#   ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="TimesRepeatBlock" parent="Object">
        <method selector="value:">
            <block arity="1">
                <parameter order="1" name="arg"/>
                <assign order="1">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="arg"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="trp"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="TimesRepeatBlock"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="t"/>
                    <expr>
                        <send selector="timesRepeat:">
                            <arg order="1">
                                <expr>
                                    <var name="trp"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="Integer" value="5"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "12345"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



# ************* MORE HARDCORE SHIZO TESTS BY @alklk ***************

def test_shizo1(tmp_path):
# class BlockOne : Block {}

# class BlockTwo : BlockOne {}

# class Main : Object {
#   run [|
#     b1 := BlockOne from: [:arg1:arg2 | _ := (arg1 concatenateWith: arg2) print. ].
#     b2 := BlockTwo from: b1.
#     _ := b2 value: 'ahoj' value: ', toto je shizo test'.
#   ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="BlockOne" parent="Block"/>
    <class name="BlockTwo" parent="BlockOne"/>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="b1"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <block arity="2">
                                        <parameter order="1" name="arg1"/>
                                        <parameter order="2" name="arg2"/>
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <send selector="concatenateWith:">
                                                            <arg order="1">
                                                                <expr>
                                                                    <var name="arg2"/>
                                                                </expr>
                                                            </arg>
                                                            <expr>
                                                                <var name="arg1"/>
                                                            </expr>
                                                        </send>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="BlockOne"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="b2"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <var name="b1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="BlockTwo"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="value:value:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="ahoj"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="String" value=", toto je shizo test"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="b2"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ahoj, toto je shizo test"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_shizo2(tmp_path):
# class Main : Object {
#   run [|
#     b := ([:arg1:arg2 |]) value: 'ahoj'.
#     _ := (b value) print.
#   ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="b"/>
                    <expr>
                        <send selector="value:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="ahoj"/>
                                </expr>
                            </arg>
                            <expr>
                                <block arity="2">
                                    <parameter order="1" name="arg1"/>
                                    <parameter order="2" name="arg2"/>
                                </block>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="value">
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

    expected_output = "ahoj"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_shizo3(tmp_path):
# class Main : Object {
#   run [|
#     _ := self b1: [:arg | _ := arg print.].
#     _ := self b2: [| _ := self b1.].
#     b3 := [| _ := self b2.].
#     _ := ((b3 value) value) value: 'ahoj'.
#   ]
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
                        <send selector="b1:">
                            <arg order="1">
                                <expr>
                                    <block arity="1">
                                        <parameter order="1" name="arg"/>
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <var name="arg"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
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
                        <send selector="b2:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="b1">
                                                    <expr>
                                                        <var name="self"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="b3"/>
                    <expr>
                        <block arity="0">
                            <assign order="1">
                                <var name="_"/>
                                <expr>
                                    <send selector="b2">
                                        <expr>
                                            <var name="self"/>
                                        </expr>
                                    </send>
                                </expr>
                            </assign>
                        </block>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="value:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="ahoj"/>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="value">
                                    <expr>
                                        <send selector="value">
                                            <expr>
                                                <var name="b3"/>
                                            </expr>
                                        </send>
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

    expected_output = "ahoj"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

def test_empty_block_returns_nil(tmp_path):

# class Main : Object {
#     run [|
#         block := [|].
#         x := block value.
#         y := Nil new.
#
#         a := (x identicalTo: y) 
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="utf-8"?>
<program language="SOL25">
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="block"/>
          <expr>
            <block arity="0"/>
          </expr>
        </assign>
        <assign order="2">
          <var name="x"/>
          <expr>
            <send selector="value">
              <expr>
                <var name="block"/>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="y"/>
          <expr>
            <send selector="new">
              <expr>
                <literal class="class" value="Nil"/>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="4">
          <var name="a"/>
          <expr>
            <send selector="ifTrue:ifFalse:">
              <arg order="1">
                <expr>
                  <block arity="0">
                    <assign order="1">
                      <var name="_"/>
                      <expr>
                        <send selector="print">
                          <expr>
                            <literal class="String" value="ANO"/>
                          </expr>
                        </send>
                      </expr>
                    </assign>
                  </block>
                </expr>
              </arg>
              <arg order="2">
                <expr>
                  <block arity="0">
                    <assign order="1">
                      <var name="_"/>
                      <expr>
                        <send selector="print">
                          <expr>
                            <literal class="String" value="NE"/>
                          </expr>
                        </send>
                      </expr>
                    </assign>
                  </block>
                </expr>
              </arg>
              <expr>
                <send selector="identicalTo:">
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
            </send>
          </expr>
        </assign>
      </block>
    </method>
  </class>
</program>

""".lstrip()

    expected_output = "ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


# ************************ LeO tests ***********************

def test_leo_nil_var_print(tmp_path):
# class Main : Object {
#   run [ |
#     result := nil.
#     _ := ((result asString) print).
#   ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="result" />
          <expr>
            <literal class="Nil" value="nil" />
          </expr>
        </assign>
        <assign order="2">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <var name="result" />
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

    expected_output = "nil"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_leo_string_constructors(tmp_path):
# class Main : Object {
#   run [ |
#     _ := ('[' print).
#     str := (String new).
#     _ := (str print).
#     _ := (']' print).
#     inputString := (String read).
#     _ := (inputString print).
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
            <send selector="print">
              <expr>
                <literal class="String" value="[" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="str" />
          <expr>
            <send selector="new">
              <expr>
                <literal class="class" value="String" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <var name="str" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="4">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value="]" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="5">
          <var name="inputString" />
          <expr>
            <send selector="read">
              <expr>
                <literal class="class" value="String" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="6">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <var name="inputString" />
              </expr>
            </send>
          </expr>
        </assign>
      </block>
    </method>
  </class>
</program>
""".lstrip()

    expected_output = "[]Hello, world!"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("Hello, world!")

    run_test(str(input_file), input_text, expected_output)


def test_leo_escape_sequence(tmp_path):
# class Main : Object {
#   run [ |
#     i := '<>interpreted (\n, \\, \')'.
#     _ := (i print).
#   ]
# }
    input_text = r"""
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="i" />
          <expr>
            <literal class="String" value="&lt;&gt;interpreted (\n, \\, \')" />
          </expr>
        </assign>
        <assign order="2">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <var name="i" />
              </expr>
            </send>
          </expr>
        </assign>
      </block>
    </method>
  </class>
</program>
""".lstrip()

    expected_output = r"""<>interpreted (
, \, ')"""

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_leo_attribute_individuality(tmp_path):
# class TestClass : Object {

# }

# class Main : Object {
#   run [ |
#     instance1 := (TestClass new).
#     instance2 := (TestClass new).
#     _ := (instance1 attribute: 5).
#     _ := (instance2 attribute: 10).
#     value1 := (instance1 attribute).
#     value2 := (instance2 attribute).
#     _ := ((value1 asString) print).
#     _ := ('\n' print).
#     _ := ((value2 asString) print).
#     _ := ('\n' print).
#   ]
# }
    input_text = r"""
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="TestClass" parent="Object" />
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="instance1" />
          <expr>
            <send selector="new">
              <expr>
                <literal class="class" value="TestClass" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="instance2" />
          <expr>
            <send selector="new">
              <expr>
                <literal class="class" value="TestClass" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <send selector="attribute:">
              <expr>
                <var name="instance1" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="Integer" value="5" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="4">
          <var name="_" />
          <expr>
            <send selector="attribute:">
              <expr>
                <var name="instance2" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="Integer" value="10" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="5">
          <var name="value1" />
          <expr>
            <send selector="attribute">
              <expr>
                <var name="instance1" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="6">
          <var name="value2" />
          <expr>
            <send selector="attribute">
              <expr>
                <var name="instance2" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="7">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <var name="value1" />
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="8">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value="\n" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="9">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <var name="value2" />
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="10">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value="\n" />
              </expr>
            </send>
          </expr>
        </assign>
      </block>
    </method>
  </class>
</program>
""".lstrip()

    expected_output = "5\n10"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_leo_self_attributes(tmp_path):
# class Main : Object {
#   run [ |
#     r := (self value: 10).
#     _ := (((self value) asString) print).
#     e := (self next: (self value)).
#     t := (self value: nil).
#     _ := (((self next) asString) print).
#     _ := (((self value) asString) print).
#   ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="r" />
          <expr>
            <send selector="value:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="Integer" value="10" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <send selector="value">
                      <expr>
                        <var name="self" />
                      </expr>
                    </send>
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="e" />
          <expr>
            <send selector="next:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <send selector="value">
                    <expr>
                      <var name="self" />
                    </expr>
                  </send>
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="4">
          <var name="t" />
          <expr>
            <send selector="value:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="Nil" value="nil" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="5">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <send selector="next">
                      <expr>
                        <var name="self" />
                      </expr>
                    </send>
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="6">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <send selector="value">
                      <expr>
                        <var name="self" />
                      </expr>
                    </send>
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

    expected_output = "1010nil"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_leo_self_identicalTo(tmp_path):
# class CustomClass : Object {
#   returnSelf [ |
#     _ := self.
#   ]
# }

# class Main : Object {
#   run [ |
#     _ := (true string: 'true').
#     _ := (false string: 'false').
#     instance := (CustomClass new).
#     returnedSelf := (instance returnSelf).
#     result := (instance identicalTo: returnedSelf).
#     _ := ((result string) print).
#   ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="CustomClass" parent="Object">
    <method selector="returnSelf">
      <block arity="0">
        <assign order="1">
          <var name="_" />
          <expr>
            <var name="self" />
          </expr>
        </assign>
      </block>
    </method>
  </class>
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="_" />
          <expr>
            <send selector="string:">
              <expr>
                <literal class="True" value="true" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="String" value="true" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="_" />
          <expr>
            <send selector="string:">
              <expr>
                <literal class="False" value="false" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="String" value="false" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="instance" />
          <expr>
            <send selector="new">
              <expr>
                <literal class="class" value="CustomClass" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="4">
          <var name="returnedSelf" />
          <expr>
            <send selector="returnSelf">
              <expr>
                <var name="instance" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="5">
          <var name="result" />
          <expr>
            <send selector="identicalTo:">
              <expr>
                <var name="instance" />
              </expr>
              <arg order="1">
                <expr>
                  <var name="returnedSelf" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="6">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="string">
                  <expr>
                    <var name="result" />
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

    expected_output = "true"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

def test_leo_isNumber(tmp_path):
# class Main : Object {
#   run [ |
#     integerInstance := (Integer new).
#     stringInstance := (String new).
#     _ := (true string: 'true').
#     _ := (false string: 'false').
#     isIntegerNumber := (integerInstance isNumber).
#     isStringNumber := (stringInstance isNumber).
#     _ := ((isIntegerNumber string) print).
#     _ := ('\n' print).
#     _ := ((isStringNumber string) print).
#     _ := ('\n' print).
#     _ := ((((Object new) isNumber) string) print).
#   ]
# }
    input_text = r"""
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="integerInstance" />
          <expr>
            <send selector="new">
              <expr>
                <literal class="class" value="Integer" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="stringInstance" />
          <expr>
            <send selector="new">
              <expr>
                <literal class="class" value="String" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <send selector="string:">
              <expr>
                <literal class="True" value="true" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="String" value="true" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="4">
          <var name="_" />
          <expr>
            <send selector="string:">
              <expr>
                <literal class="False" value="false" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="String" value="false" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="5">
          <var name="isIntegerNumber" />
          <expr>
            <send selector="isNumber">
              <expr>
                <var name="integerInstance" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="6">
          <var name="isStringNumber" />
          <expr>
            <send selector="isNumber">
              <expr>
                <var name="stringInstance" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="7">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="string">
                  <expr>
                    <var name="isIntegerNumber" />
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="8">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value="\n" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="9">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="string">
                  <expr>
                    <var name="isStringNumber" />
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="10">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value="\n" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="11">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="string">
                  <expr>
                    <send selector="isNumber">
                      <expr>
                        <send selector="new">
                          <expr>
                            <literal class="class" value="Object" />
                          </expr>
                        </send>
                      </expr>
                    </send>
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

    expected_output = """true
false
false"""

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_leo_block_1par_eval(tmp_path):
# class Main : Object {
#   run [ |
#     block := [ :param|
#       _ := param.
#     ].
#     argument := 42.
#     result := (block value: argument).
#     _ := ((result asString) print).
#   ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="block" />
          <expr>
            <block arity="1">
              <parameter order="1" name="param" />
              <assign order="1">
                <var name="_" />
                <expr>
                  <var name="param" />
                </expr>
              </assign>
            </block>
          </expr>
        </assign>
        <assign order="2">
          <var name="argument" />
          <expr>
            <literal class="Integer" value="42" />
          </expr>
        </assign>
        <assign order="3">
          <var name="result" />
          <expr>
            <send selector="value:">
              <expr>
                <var name="block" />
              </expr>
              <arg order="1">
                <expr>
                  <var name="argument" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="4">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <var name="result" />
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

    expected_output = "42"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_leo_super_cascade(tmp_path):
# class CustomClass : Object {
#   testMethod [ |
#     _ := 'Superclass method called.'.
#   ]
# }

# class MiddleClass : CustomClass {
#   testMethod [ |
#     superResult := (super testMethod).
#     result := (superResult concatenateWith: ' Middleclass method extended.').
#     _ := result.
#   ]
# }

# class SubClass : MiddleClass {
#   testMethod [ |
#     superResult := (super testMethod).
#     result := (superResult concatenateWith: ' Subclass method extended.').
#     _ := result.
#   ]
# }

# class Main : Object {
#   run [ |
#     subInstance := (SubClass new).
#     result := (subInstance testMethod).
#     _ := (result print).
#   ]
# }
    input_text = r"""
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="CustomClass" parent="Object">
    <method selector="testMethod">
      <block arity="0">
        <assign order="1">
          <var name="_" />
          <expr>
            <literal class="String" value="Superclass method called." />
          </expr>
        </assign>
      </block>
    </method>
  </class>
  <class name="MiddleClass" parent="CustomClass">
    <method selector="testMethod">
      <block arity="0">
        <assign order="1">
          <var name="superResult" />
          <expr>
            <send selector="testMethod">
              <expr>
                <var name="super" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="result" />
          <expr>
            <send selector="concatenateWith:">
              <expr>
                <var name="superResult" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="String" value=" Middleclass method extended." />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <var name="result" />
          </expr>
        </assign>
      </block>
    </method>
  </class>
  <class name="SubClass" parent="MiddleClass">
    <method selector="testMethod">
      <block arity="0">
        <assign order="1">
          <var name="superResult" />
          <expr>
            <send selector="testMethod">
              <expr>
                <var name="super" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="result" />
          <expr>
            <send selector="concatenateWith:">
              <expr>
                <var name="superResult" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="String" value=" Subclass method extended." />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <var name="result" />
          </expr>
        </assign>
      </block>
    </method>
  </class>
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="subInstance" />
          <expr>
            <send selector="new">
              <expr>
                <literal class="class" value="SubClass" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="result" />
          <expr>
            <send selector="testMethod">
              <expr>
                <var name="subInstance" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <var name="result" />
              </expr>
            </send>
          </expr>
        </assign>
      </block>
    </method>
  </class>
</program>
""".lstrip()

    expected_output = "Superclass method called. Middleclass method extended. Subclass method extended."

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_leo_super_main(tmp_path):
# class Test : Object {
#   run [ |
#     _ := ('Test run' print).
#   ]
# }

# class Main : Test {
#   run [ |
#     _ := (super run).
#     _ := ('\nMain run' print).
#   ]
# }
    input_text = r"""
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="Test" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value="Test run" />
              </expr>
            </send>
          </expr>
        </assign>
      </block>
    </method>
  </class>
  <class name="Main" parent="Test">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="_" />
          <expr>
            <send selector="run">
              <expr>
                <var name="super" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value="\nMain run" />
              </expr>
            </send>
          </expr>
        </assign>
      </block>
    </method>
  </class>
</program>
""".lstrip()

    expected_output = """Test run
Main run"""

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_leo_mystring(tmp_path):
# class MyString : String {
#   init [ |
#     _ := (self isMyString: true).
#     _ := (self length: 0).
#     _ := self.
#   ]
#   init: [ :len|
#     _ := (self init).
#     _ := (self length: len).
#     _ := self.
#   ]
#   concatenateWith: [ :s|
#     res := (MyString from: (super concatenateWith: s)).
#     _ := (res init: ((self length) plus: (s length))).
#   ]
#   startsWith:endsBefore: [ :b :e|
#     res := (super startsWith: b endsBefore: e).
#     _ := self tmp_res: res.
#     _ := self tmp_len: (e minus: b).
#     _ := ((res isNil) ifTrue: [ |
#     ] ifFalse: [ |
#       _ := self tmp_res: (MyString from: (self tmp_res)).
#       _ := (self tmp_res) init: (self tmp_len).
#     ]).

#     _ := self tmp_res.
#   ]
#   println [ |
#     _ := (self print).
#     _ := ('\n' print).
#     _ := self.
#   ]
# }

# class Main : Object {
#   run [ |
#     ms := ((MyString new) init).
#     ms2 := ((MyString from: 'ahoj') init: 4).
#     ms3 := ((MyString from: 'svete') init: 5).

#     cat := (ms concatenateWith: ms2).
#     _ := (cat print).
#     _ := (' je delky ' print).
#     _ := (((cat length) asString) print).
#     _ := '\n' print.

#     spoj := (cat concatenateWith: ms3).
#     _ := (spoj println).
#     _ := (((spoj length) asString) print).
#     _ := '\n' print.

#     substr := (spoj startsWith: 3 endsBefore: 9).
#     _ := substr print.
#     _ := ' je delky ' print.
#     _ := (((substr length) asString) print).
#   ]
# }
    input_text = r"""
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="MyString" parent="String">
    <method selector="init">
      <block arity="0">
        <assign order="1">
          <var name="_" />
          <expr>
            <send selector="isMyString:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="True" value="true" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="_" />
          <expr>
            <send selector="length:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="Integer" value="0" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <var name="self" />
          </expr>
        </assign>
      </block>
    </method>
    <method selector="init:">
      <block arity="1">
        <parameter order="1" name="len" />
        <assign order="1">
          <var name="_" />
          <expr>
            <send selector="init">
              <expr>
                <var name="self" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="_" />
          <expr>
            <send selector="length:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <var name="len" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <var name="self" />
          </expr>
        </assign>
      </block>
    </method>
    <method selector="concatenateWith:">
      <block arity="1">
        <parameter order="1" name="s" />
        <assign order="1">
          <var name="res" />
          <expr>
            <send selector="from:">
              <expr>
                <literal class="class" value="MyString" />
              </expr>
              <arg order="1">
                <expr>
                  <send selector="concatenateWith:">
                    <expr>
                      <var name="super" />
                    </expr>
                    <arg order="1">
                      <expr>
                        <var name="s" />
                      </expr>
                    </arg>
                  </send>
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="_" />
          <expr>
            <send selector="init:">
              <expr>
                <var name="res" />
              </expr>
              <arg order="1">
                <expr>
                  <send selector="plus:">
                    <expr>
                      <send selector="length">
                        <expr>
                          <var name="self" />
                        </expr>
                      </send>
                    </expr>
                    <arg order="1">
                      <expr>
                        <send selector="length">
                          <expr>
                            <var name="s" />
                          </expr>
                        </send>
                      </expr>
                    </arg>
                  </send>
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
      </block>
    </method>
    <method selector="startsWith:endsBefore:">
      <block arity="2">
        <parameter order="1" name="b" />
        <parameter order="2" name="e" />
        <assign order="1">
          <var name="res" />
          <expr>
            <send selector="startsWith:endsBefore:">
              <expr>
                <var name="super" />
              </expr>
              <arg order="1">
                <expr>
                  <var name="b" />
                </expr>
              </arg>
              <arg order="2">
                <expr>
                  <var name="e" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="_" />
          <expr>
            <send selector="tmp_res:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <var name="res" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <send selector="tmp_len:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <send selector="minus:">
                    <expr>
                      <var name="e" />
                    </expr>
                    <arg order="1">
                      <expr>
                        <var name="b" />
                      </expr>
                    </arg>
                  </send>
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="4">
          <var name="_" />
          <expr>
            <send selector="ifTrue:ifFalse:">
              <expr>
                <send selector="isNil">
                  <expr>
                    <var name="res" />
                  </expr>
                </send>
              </expr>
              <arg order="1">
                <expr>
                  <block arity="0" />
                </expr>
              </arg>
              <arg order="2">
                <expr>
                  <block arity="0">
                    <assign order="1">
                      <var name="_" />
                      <expr>
                        <send selector="tmp_res:">
                          <expr>
                            <var name="self" />
                          </expr>
                          <arg order="1">
                            <expr>
                              <send selector="from:">
                                <expr>
                                  <literal class="class" value="MyString" />
                                </expr>
                                <arg order="1">
                                  <expr>
                                    <send selector="tmp_res">
                                      <expr>
                                        <var name="self" />
                                      </expr>
                                    </send>
                                  </expr>
                                </arg>
                              </send>
                            </expr>
                          </arg>
                        </send>
                      </expr>
                    </assign>
                    <assign order="2">
                      <var name="_" />
                      <expr>
                        <send selector="init:">
                          <expr>
                            <send selector="tmp_res">
                              <expr>
                                <var name="self" />
                              </expr>
                            </send>
                          </expr>
                          <arg order="1">
                            <expr>
                              <send selector="tmp_len">
                                <expr>
                                  <var name="self" />
                                </expr>
                              </send>
                            </expr>
                          </arg>
                        </send>
                      </expr>
                    </assign>
                  </block>
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="5">
          <var name="_" />
          <expr>
            <send selector="tmp_res">
              <expr>
                <var name="self" />
              </expr>
            </send>
          </expr>
        </assign>
      </block>
    </method>
    <method selector="println">
      <block arity="0">
        <assign order="1">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <var name="self" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value="\n" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <var name="self" />
          </expr>
        </assign>
      </block>
    </method>
  </class>
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="ms" />
          <expr>
            <send selector="init">
              <expr>
                <send selector="new">
                  <expr>
                    <literal class="class" value="MyString" />
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="ms2" />
          <expr>
            <send selector="init:">
              <expr>
                <send selector="from:">
                  <expr>
                    <literal class="class" value="MyString" />
                  </expr>
                  <arg order="1">
                    <expr>
                      <literal class="String" value="ahoj" />
                    </expr>
                  </arg>
                </send>
              </expr>
              <arg order="1">
                <expr>
                  <literal class="Integer" value="4" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="ms3" />
          <expr>
            <send selector="init:">
              <expr>
                <send selector="from:">
                  <expr>
                    <literal class="class" value="MyString" />
                  </expr>
                  <arg order="1">
                    <expr>
                      <literal class="String" value="svete" />
                    </expr>
                  </arg>
                </send>
              </expr>
              <arg order="1">
                <expr>
                  <literal class="Integer" value="5" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="4">
          <var name="cat" />
          <expr>
            <send selector="concatenateWith:">
              <expr>
                <var name="ms" />
              </expr>
              <arg order="1">
                <expr>
                  <var name="ms2" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="5">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <var name="cat" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="6">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value=" je delky " />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="7">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <send selector="length">
                      <expr>
                        <var name="cat" />
                      </expr>
                    </send>
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="8">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value="\n" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="9">
          <var name="spoj" />
          <expr>
            <send selector="concatenateWith:">
              <expr>
                <var name="cat" />
              </expr>
              <arg order="1">
                <expr>
                  <var name="ms3" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="10">
          <var name="_" />
          <expr>
            <send selector="println">
              <expr>
                <var name="spoj" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="11">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <send selector="length">
                      <expr>
                        <var name="spoj" />
                      </expr>
                    </send>
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="12">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value="\n" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="13">
          <var name="substr" />
          <expr>
            <send selector="startsWith:endsBefore:">
              <expr>
                <var name="spoj" />
              </expr>
              <arg order="1">
                <expr>
                  <literal class="Integer" value="3" />
                </expr>
              </arg>
              <arg order="2">
                <expr>
                  <literal class="Integer" value="9" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="14">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <var name="substr" />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="15">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <literal class="String" value=" je delky " />
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="16">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <send selector="length">
                      <expr>
                        <var name="substr" />
                      </expr>
                    </send>
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

    expected_output = """ahoj je delky 4
ahojsvete
9
ojsvet je delky 6"""

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_leo_factorial_iterative(tmp_path):
# class Main : Object {
#   run [ |
#     n := ((String read) asInteger).
#     res := (self factorial: n).
#     _ := ((res asString) print).
#   ]
#   decrement_a [ |
#     _ := (self a: ((self a) minus: 1)).
#   ]
#   multiply_vysl_a [ |
#     _ := (self vysl: ((self vysl) multiplyBy: (self a))).
#   ]
#   factorial: [ :n|
#     _ := (self a: n).
#     r := ((n greaterThan: 0) ifTrue: [ |
#       _ := (self vysl: 1).
#       _ := ([ |
#         _ := ((self a) greaterThan: 0).
#       ] whileTrue: [ |
#         _ := (self multiply_vysl_a).
#         _ := (self decrement_a).
#       ]).
#     ] ifFalse: [ |
#       _ := ('Factorial nelze spocitat.' print).
#     ]).
#     _ := (self vysl).
#   ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
  <class name="Main" parent="Object">
    <method selector="run">
      <block arity="0">
        <assign order="1">
          <var name="n" />
          <expr>
            <send selector="asInteger">
              <expr>
                <send selector="read">
                  <expr>
                    <literal class="class" value="String" />
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="res" />
          <expr>
            <send selector="factorial:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <var name="n" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <send selector="print">
              <expr>
                <send selector="asString">
                  <expr>
                    <var name="res" />
                  </expr>
                </send>
              </expr>
            </send>
          </expr>
        </assign>
      </block>
    </method>
    <method selector="decrement_a">
      <block arity="0">
        <assign order="1">
          <var name="_" />
          <expr>
            <send selector="a:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <send selector="minus:">
                    <expr>
                      <send selector="a">
                        <expr>
                          <var name="self" />
                        </expr>
                      </send>
                    </expr>
                    <arg order="1">
                      <expr>
                        <literal class="Integer" value="1" />
                      </expr>
                    </arg>
                  </send>
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
      </block>
    </method>
    <method selector="multiply_vysl_a">
      <block arity="0">
        <assign order="1">
          <var name="_" />
          <expr>
            <send selector="vysl:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <send selector="multiplyBy:">
                    <expr>
                      <send selector="vysl">
                        <expr>
                          <var name="self" />
                        </expr>
                      </send>
                    </expr>
                    <arg order="1">
                      <expr>
                        <send selector="a">
                          <expr>
                            <var name="self" />
                          </expr>
                        </send>
                      </expr>
                    </arg>
                  </send>
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
      </block>
    </method>
    <method selector="factorial:">
      <block arity="1">
        <parameter order="1" name="n" />
        <assign order="1">
          <var name="_" />
          <expr>
            <send selector="a:">
              <expr>
                <var name="self" />
              </expr>
              <arg order="1">
                <expr>
                  <var name="n" />
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="2">
          <var name="r" />
          <expr>
            <send selector="ifTrue:ifFalse:">
              <expr>
                <send selector="greaterThan:">
                  <expr>
                    <var name="n" />
                  </expr>
                  <arg order="1">
                    <expr>
                      <literal class="Integer" value="0" />
                    </expr>
                  </arg>
                </send>
              </expr>
              <arg order="1">
                <expr>
                  <block arity="0">
                    <assign order="1">
                      <var name="_" />
                      <expr>
                        <send selector="vysl:">
                          <expr>
                            <var name="self" />
                          </expr>
                          <arg order="1">
                            <expr>
                              <literal class="Integer" value="1" />
                            </expr>
                          </arg>
                        </send>
                      </expr>
                    </assign>
                    <assign order="2">
                      <var name="_" />
                      <expr>
                        <send selector="whileTrue:">
                          <expr>
                            <block arity="0">
                              <assign order="1">
                                <var name="_" />
                                <expr>
                                  <send selector="greaterThan:">
                                    <expr>
                                      <send selector="a">
                                        <expr>
                                          <var name="self" />
                                        </expr>
                                      </send>
                                    </expr>
                                    <arg order="1">
                                      <expr>
                                        <literal class="Integer" value="0" />
                                      </expr>
                                    </arg>
                                  </send>
                                </expr>
                              </assign>
                            </block>
                          </expr>
                          <arg order="1">
                            <expr>
                              <block arity="0">
                                <assign order="1">
                                  <var name="_" />
                                  <expr>
                                    <send selector="multiply_vysl_a">
                                      <expr>
                                        <var name="self" />
                                      </expr>
                                    </send>
                                  </expr>
                                </assign>
                                <assign order="2">
                                  <var name="_" />
                                  <expr>
                                    <send selector="decrement_a">
                                      <expr>
                                        <var name="self" />
                                      </expr>
                                    </send>
                                  </expr>
                                </assign>
                              </block>
                            </expr>
                          </arg>
                        </send>
                      </expr>
                    </assign>
                  </block>
                </expr>
              </arg>
              <arg order="2">
                <expr>
                  <block arity="0">
                    <assign order="1">
                      <var name="_" />
                      <expr>
                        <send selector="print">
                          <expr>
                            <literal class="String" value="Factorial nelze spocitat." />
                          </expr>
                        </send>
                      </expr>
                    </assign>
                  </block>
                </expr>
              </arg>
            </send>
          </expr>
        </assign>
        <assign order="3">
          <var name="_" />
          <expr>
            <send selector="vysl">
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

    expected_output = "720"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("6")

    run_test(str(input_file), input_text, expected_output)
