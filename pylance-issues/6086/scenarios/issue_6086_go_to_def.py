class ClassWithMagicMethod:
    def __len__(self) -> int:
        return 1

print(len(ClassWithMagicMethod()))
