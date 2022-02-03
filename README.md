
<div align="center">
  <img style="text-align:center" src="hascal-logo.png" height="128px" width="128px">


  # The Hascal Programming Language

  [Website](https://hascal.github.io) |
  [Docs](https://hascal.github.io/docs/latest) |
  [Changelog](docs/CHANGELOG.md)

  [IDE Integration](docs/ide.md) |
  [Library Index](https://github.com/hascal/libs)

  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://LinkedIn.com/in/company/hascal-lang)
  [![Gitter](https://img.shields.io/gitter/room/hascal/community?style=for-the-badge)](https://gitter.im/hascal/community)
  
</div>

**Hascal** is a general purpose and open source programming language designed to build optimal, maintainable, reliable and efficient software.
> **NOTES:** 
> - Hascal pronounces like "Pascal".
> - Hascal is still in the very early stages of development.
## Features
- [x] Simple and easy to learn
- [x] Fast and powerful like C++
- [x] Inspired by Swift and Pascal
- [x] C++ on backend
- [x] Compatible with C\C++\Obj-C

## Examples
Hello World :
```typescript
function main() : int {
    print("Hello World!")
    return 0
}
```

Formatting Strings :
```typescript
function main() : int {
    var name = ReadStr("Enter your name :")
    var fmt_str = format("Hi,{}",name)
    print(fmt_str)
    return 0
}
```

HTTP Response :
```typescript
use http

function main(): int {
    print(get("http://example.com"))
    return 0
}
```

> You can see more Hascal examples in [examples folder](https://github.com/hascal/hascal/tree/main/examples).

## Documentation
> You can find Hascal's documentation, [Here](https://hascal.github.io/docs)

## Contributions
Any contribution is welcome :)

[See our roadmap](docs/roadmap.md)

<!-- [![graph](https://contrib.rocks/image?repo=hascal/hascal)](https://github.com/hascal/hascal/graphs/contributors)
-->
## License
The compiler and the standard libraries are licensed under the **"MIT License"**,
Read the [License](https://github.com/hascal/hascal/blob/main/LICENSE) for more information.

## About
Copyright © 2019-2022 **Hascal Foundation**, \
all rights reserved.

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
