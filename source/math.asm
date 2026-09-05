.global asm_add
asm_add:
    add r3, r3, r4
    blr

.global asm_mul
asm_mul:
    mullw r3, r3, r4
    blr

.global asm_sub
asm_sub:
    sub r3, r3, r4
    blr