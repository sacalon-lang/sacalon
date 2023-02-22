# Hascal's Changelog

<details>
<summary>v1.4.2</summary>

#### New features

#### Changes
- observe [Hasca's coding style](https://hascal.github.io/style.html) in libraries

#### Bug fixes

#### Removed

</details>

<details>
<summary>v1.4.1</summary>

#### Bug fixes
- No errors when main doesn't return anything #67 (by @mehanalavimajd )

</details>

<details>
<summary>v1.4.0</summary>

#### New features
- add builtin range function
```typescript
function main(): int {
    // prints 1 to 10
    for i in range(1,11){
        print(i)
    }
    return 0
}
```
- add `asin`, `acos`, `asinh`, `acosh`, `exp`, `frexpr`, `ldexp`, `log`, `log10`, `fdim`, `sqrt`, `ceil`, `floor`, `NaN`, `max`, `min` functions to `math` library, [see documentation](https://hascal.github.io/docs/latest/stdlib/math.html).
- Showing error for overloading function's return type.

#### Changes
- Speedup parsing and compiling

#### Bug fixes
- fix passing list to `for in` statement

#### Removed

</details>

---

<details>
<summary>v1.3.12</summary>

#### New features
- add support for multiline C-style comment
- add `round` function to `math` library

#### Changes
- Hascal relicensed from MIT license to BSD-3-Clause license

#### Bug fixes
- fix string subscripting bug
- fix empty list parsing bug
- fix random library bugs

#### Removed

</details>

---

<details>
<summary>v1.3.11</summary>

#### New features
- add uniform distribution based random number generator called `uniform` in `random` library

#### Changes
- change `static` decorator name to `static_function` name
- rename `times` function to `multiplies` in `functional` library
- rename `if_and`, `if_or`, `if_not` functions to `_and`, `_or`, `_not` in `functional` library

#### Bug fixes
- fix package manager bug

#### Removed

</details>

---

<details>
<summary>v1.3.10</summary>

#### New features
- show error for undeleted variables from heap

#### Changes
- improve `math`,`os` library
- in `functional` library : change `lessThanOrEqual` to `lessThanEqual`, `greaterThanOrEqual` to `greaterThanEqual`
- improve error handler for conditions
- `pytest` based test runner(@mmdbalkhi)
- fix conflicting with C\C++\Obj-C in FFI features
- change `static` decorator name to `static_function` name

#### Bug fixes
- fix `math` library bug
- fix import package bug with `_.*` name
- fix `crypto.sha256` library bug

#### Removed
- remove `libtcc` from stdlib

</details>

---

<details>
<summary>v1.3.9x</summary>

<details>
<summary>v1.3.9</summary>

#### New features
- add `hascal list` command to list all available packages
- add `hascal init` command to create a new project, that generates `config.json`, `.gitignore` and `src/app.has` files
- add `hascal build` command to build project
- add `hascal run` command to run project
- add `string_reverse(str:string)` function to `strings` module
- add `assert` function to runtime library
- add `no_std` compiler option
- add `filename` config option

#### Changes
- change emitting `std::string` for strings to `string`(because in showing assertion errors, `std::string` is illusory).
- use `sys.exit` instead of `exit` in `src/core/h_help.py`(@mmdbalkhi)
- fix importing system bugs
- improve `typeof` builtin function
<!-- - remove file extension (`.has`) checking #42 -->

#### Bug fixes
- fix assigning `NULL` to arrays and pointers bug, #36.
- fix `check_g++` config option bugs
- fix not defined consts when importing packages
- fix `random` library bug
- fix `browser` library bug

#### Removed
- remove `windows`,`browser` libraries

</details>

<details>
<summary>v1.3.9-rc.2</summary>

#### Bug fixes
- fix a critical bug in importing system

</details>

<details>
<summary>v1.3.9-rc.1</summary>

#### Changes
- upgrade importing system
- some changes in self hosted compiler(NOTE: self hosted compiler is not ready yet)

#### Bug fixes
- fix import bug when importing one package in multiple files
- fix self hosted bugs

</details>

<details>
<summary>v1.3.9-rc</summary>

#### Changes
- Rewrite package manager

#### Bug fixes
- fix `http` library bug
- fix cpp importing bug

</details>

<details>
<summary>v1.3.9-beta</summary>

#### New features
- passing functions as arguments
```typescript
function f(x: int): int {
    return x + 1
}

function g(func:Function[int]int): int {
    return func(1)
}
```
- add static variables, [See this example](https://github.com/hascal/hascal/blob/main/tests/static.has)
- add `only_compile` config option

#### Changes
- upgrade importing system

#### Bug fixes
- fix pyinstaller build issue

#### Removed

</details>

<details>
<summary>v1.3.9-alpha.1</summary>

#### Changes
- add `download`,`upload`,`post` functions to `http` library
- `https` support for `http` library
- add `windows` library(that includes `windows.h`)
- add `browser` library to open urls in default browser(now only supports windows)

#### Bug fixes
- fix linker flag import bug in `cuse` statement

</details>

</details>

<hr>

<details>
<summary>v1.3.8</summary>

#### New features
- non-nullable and nullable variables

#### Changes
- change pointer unary from `*` to `^`
- improve importing system

#### Bug fixes
- fix repetitious imports bug
- fix #29 bug(by [@mmdbalkhi](https://github.com/mmdbalkhi))
  
#### Removed
- remove `token` library

</details>

<hr>

<details>
<summary>v1.3.7</summary>

#### New features
- manual memory management with `new` and `delete` keyword
- functional programming paradigm
- speed up compilation time
- add `typeof` function
- now can print arrays and structures
- function decorators
- `static` and `extern` decorator
- multiple library import
- improve importing system
- improve stdlib architecture

#### Bug fixes
- fix scoping bug
- fix `conv` library bug
- fix conditions bug

#### Removed
- `export` library removed
- `local use` statement removed

</details>

<hr>

<details>
<summary>v1.3.6</summary>
  
#### New features
- more data types : `int8`,`uint8`,`int16`,`uint16`,`int32`,`uint32`,`int64`,`uint64`,`double`
- type compatibility
- multi line string
- pointers and references
```typescript
var x : *int = 20
var y : int = 10
x = &y
var z = *x // type : int

// Pointers fix incomplete types on struct defination
struct bar {
    var self : *bar
}
```
- add `sizeof` function

#### Bug fixes
- fix lexer bugs
- check if function returns a value at end of string else show error
- `main` function should returns int
- fix `termcolor` library bugs
- fix enum bugs

#### Standart library
- add `sdl2` wrapper
- add `export` library for exporting to C(see : [haspy](https://github.com/bistcuite/haspy))
- add `crypto.sha256` for sha256 hashing

#### Removed
- `libcinfo` library removed

</details>

<hr>

<details>
<summary>v1.3.5</summary>

#### Standard library
##### Updated
`os` :
- add `compiler_name` function to get the name of the compiler
- add `arch` function to get the architecture of the system
- add `is_x86` function to check if the architecture is x86
- add `is_x64` function to check if the architecture is x64
- add `getenv` function to get an environment variable
##### Added
- add `libcinfo` library to get information about the libc
- add `termcolor` library to colorize the output

![assets/termcolor.png](assets/termcolor.png)

#### Bug fixes
- Fix incomplete type defination bug

</details>

<hr>

<details>
<summary>v1.3.4</summary>
  
#### New features
- compiler option : now can generate c++ code from hascal code with `c++_code : 1` in `config.json` file
- use `cuse` keyword to include c++ files.

#### Bug fixes
- Fix semantic analyser bugs
- Fix standard library bug

</details>

<hr>

<details>
<summary>v1.3.3</summary>

#### New features
- struct inheritance
- can use `cuse` statement on struct declaration

#### Bug fixes
- Fix variable scope bug
- Fix variable declaration bug
- Fix semantic analyser bug

</details>

<hr>

<details>
<summary>v1.3.2</summary>

#### New features
- `for in` statement
- library manager
- flag option
- `cuse` statement

#### Bug fixes
- Fix semantic analyser bugs
- Fix nested struct bug

#### Removed
- `for to` and `for downto` statement removed

</details>

<hr>

<details>
<summary>v1.3.1</summary>

#### New features
- Basic Semantic Anaslyser

#### Removed
- remove semicolon from syntax

</details>
