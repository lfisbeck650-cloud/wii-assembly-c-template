#include <stdio.h>
#include <stdlib.h>
#include <gccore.h>
#include <wiiuse/wpad.h>

extern int asm_add(int a, int b);
extern int asm_mul(int a, int b);
extern int asm_sub(int a, int b);

static void *xfb = NULL;
static GXRModeObj *rmode = NULL;

int main(void)
{
    VIDEO_Init();
    WPAD_Init();

    rmode = VIDEO_GetPreferredMode(NULL);

    xfb = MEM_K0_TO_K1(
        SYS_AllocateFramebuffer(rmode)
    );

    console_init(
        xfb,
        20,
        20,
        rmode->fbWidth,
        rmode->xfbHeight,
        rmode->fbWidth * VI_DISPLAY_PIX_SZ
    );

    VIDEO_Configure(rmode);
    VIDEO_SetNextFramebuffer(xfb);
    VIDEO_SetBlack(FALSE);
    VIDEO_Flush();
    VIDEO_WaitVSync();

    if (rmode->viTVMode & VI_NON_INTERLACE)
        VIDEO_WaitVSync();

    printf("Hello Wii World!\n\n");
    printf("asm_add(5, 7) = %d\n", asm_add(5, 7));
    printf("asm_mul(6, 7) = %d\n", asm_mul(6, 7));
    printf("asm_sub(271, 173) = %d", asm_sub(271, 173));

    while (1)
    {
        WPAD_ScanPads();

        u32 buttons = WPAD_ButtonsDown(0);

        if (buttons & WPAD_BUTTON_HOME)
            exit(0);

        VIDEO_WaitVSync();
    }

    return 0;
}