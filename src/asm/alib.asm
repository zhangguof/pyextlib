;nasm -fwin32 alib.asm 
section .text

global  _add 
_add:
	push ebp
	mov ebp, esp
	mov eax, [ebp+0x8]; arg1
	mov ecx, [ebp+0xc]; arg2
	add eax, ecx
	leave ; mov esp, ebp/pop ebp
	
	ret