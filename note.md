@import "../abstracts/mixins";

.login--main {
    display: flex;
    width: 100%;
    padding: var(--Numbers-Space-Space-0, 0px);
    justify-content: space-between;
    align-items: center;
    flex-shrink: 0;
    background: var(--Colors-bg-bg-light, #FAFAFA);
    @include mobile-screen {
        display: flex;
        flex-direction: column;
        width: 100%;
    }
    &--form {
        display: flex;
        padding: var(--Numbers-Space-Space-7, 50px) var(--Numbers-Space-Space-4, 24px);
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        gap: var(--Numbers-Space-Space-5, 36px);
        align-self: stretch;
        border-radius: var(--Numbers-Width-Size-2, 8px);
        border: 1px solid var(--Colors-stroke-border-gray, #808080);
        background: var(--Colors-bg-bg-light, #FAFAFA);
        margin: 200px 40px;
        padding: 0px 30px;
        width: 50%;
        height: 560px;
        @include mobile-screen {
            width: 90%;
            margin-top: 30px;
        }
        &--div1 {
            display: flex;
            padding: var(--Numbers-Space-Space-0, 0px);

            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            gap: var(--Numbers-Space-Space-2, 8px);
            align-self: stretch;
            margin-top: -40px;
        }
        &--div2 {
            display: flex;
            padding: var(--Numbers-Space-Space-0, 0px);
            align-items: center;
            gap: var(--Numbers-Space-Space-3, 16px);
        }
        &--div3 {
            display: flex;
            padding: var(--Numbers-Space-Space-0, 0px);
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            gap: var(--Numbers-Space-Space-3, 16px);
            align-self: stretch;
            &--user, &--pass {
                display: flex;
                padding: var(--Numbers-Space-Space-0, 0px);
                flex-direction: column;
                justify-content: center;
                align-items: flex-start;
                gap: var(--Numbers-Space-Space-2, 8px);
                align-self: stretch;
                @include mobile-screen {
                    width: 100%;
                }
            }
            &--btn button {
                display: flex;
                height: 45px;
                padding: var(--Numbers-Space-Space-2, 8px) 150px;
                justify-content: center;
                align-items: center;
                gap: 10px;
                align-self: stretch;
                border-radius: var(--Numbers-Width-Size-2, 8px);
                background: var(--gradient2, linear-gradient(180deg, #008000 0%, #052F05 100%));
                margin-top: 10px;
                width: 520px;
                /* shadow */
                box-shadow: 0px 1px 50px 0px rgba(0, 0, 0, 0.10);
                @include mobile-screen {
                    width: 120%;
                }
            }
            &--forget {
                margin-top: 0px;
                padding: 20px 0px;
                text-decoration: none;
            }
        }
    }
    &--aside {
        display: flex;
        width: 50%;
        height: 1024px;
        padding-top: var(--Numbers-Space-Space-8, 100px);
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        flex-shrink: 0;
        background: var(--Colors-bg-bg-gray-50, #BCBCBC);
        @include mobile-screen {
            width: 100%;
            margin-top: -100px;
        }
        & p {
            align-self: stretch;
            padding: 0px 20px;
        }
        &--logo {
            display: flex;
            width: 112px;
            height: 83px;
            padding: 0px 0.68px 2.81px 0.509px;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 0.034px;
            flex-shrink: 0;
            &--1 {
                width: 69.173px;
                height: 68.915px;
                flex-shrink: 0;
            }
            &--2 {
                width: 110.811px;
                height: 11.241px;
                flex-shrink: 0;
                fill: var(--Colors-bg-bg-pry, #E87C00);
            }
        }
        &--img {
            width: 100%;
            height: 539px;
            flex-shrink: 0;
        }
    }
}
#username {
    display: flex;
    padding: var(--Numbers-Space-Space-3, 16px) 20px;
    align-items: center;
    gap: 10px;
    align-self: stretch;
    border-radius: var(--Numbers-Width-Size-1, 4px);
    border: 1px solid var(--Colors-stroke-border-gray, #808080);
    background: var(--Colors-bg-bg-light, #FAFAFA);
    width: 520px;
    @include mobile-screen {
        width: 120%;

    }

}
#label--pass {
    margin-top: 20px;
}
.forget {
    margin-top: 50px;
    @include mobile-screen {
        margin-left: 6px;
    }
}
/*#password {
    @include mobile-screen {
        width: 120%;
    }
}*/