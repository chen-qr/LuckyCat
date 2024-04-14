uniswap_router_address = "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
uniswap_router_abi = [
    {
        "type": "constructor",
        "inputs": [
            {
                "name": "_factoryV2",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "factoryV3",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "_positionManager",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "_WETH9",
                "type": "address",
                "internalType": "address"
            }
        ],
        "stateMutability": "nonpayable"
    },
    {
        "name": "WETH9",
        "type": "function",
        "inputs": [],
        "outputs": [
            {
                "name": "",
                "type": "address",
                "internalType": "address"
            }
        ],
        "stateMutability": "view"
    },
    {
        "name": "approveMax",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "approveMaxMinusOne",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "approveZeroThenMax",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "approveZeroThenMaxMinusOne",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "callPositionManager",
        "type": "function",
        "inputs": [
            {
                "name": "data",
                "type": "bytes",
                "internalType": "bytes"
            }
        ],
        "outputs": [
            {
                "name": "result",
                "type": "bytes",
                "internalType": "bytes"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "checkOracleSlippage",
        "type": "function",
        "inputs": [
            {
                "name": "paths",
                "type": "bytes[]",
                "internalType": "bytes[]"
            },
            {
                "name": "amounts",
                "type": "uint128[]",
                "internalType": "uint128[]"
            },
            {
                "name": "maximumTickDivergence",
                "type": "uint24",
                "internalType": "uint24"
            },
            {
                "name": "secondsAgo",
                "type": "uint32",
                "internalType": "uint32"
            }
        ],
        "outputs": [],
        "stateMutability": "view"
    },
    {
        "name": "checkOracleSlippage",
        "type": "function",
        "inputs": [
            {
                "name": "path",
                "type": "bytes",
                "internalType": "bytes"
            },
            {
                "name": "maximumTickDivergence",
                "type": "uint24",
                "internalType": "uint24"
            },
            {
                "name": "secondsAgo",
                "type": "uint32",
                "internalType": "uint32"
            }
        ],
        "outputs": [],
        "stateMutability": "view"
    },
    {
        "name": "exactInput",
        "type": "function",
        "inputs": [
            {
                "name": "params",
                "type": "tuple",
                "components": [
                    {
                        "name": "path",
                        "type": "bytes",
                        "internalType": "bytes"
                    },
                    {
                        "name": "recipient",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "amountIn",
                        "type": "uint256",
                        "internalType": "uint256"
                    },
                    {
                        "name": "amountOutMinimum",
                        "type": "uint256",
                        "internalType": "uint256"
                    }
                ],
                "internalType": "struct IV3SwapRouter.ExactInputParams"
            }
        ],
        "outputs": [
            {
                "name": "amountOut",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "exactInputSingle",
        "type": "function",
        "inputs": [
            {
                "name": "params",
                "type": "tuple",
                "components": [
                    {
                        "name": "tokenIn",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "tokenOut",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "fee",
                        "type": "uint24",
                        "internalType": "uint24"
                    },
                    {
                        "name": "recipient",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "amountIn",
                        "type": "uint256",
                        "internalType": "uint256"
                    },
                    {
                        "name": "amountOutMinimum",
                        "type": "uint256",
                        "internalType": "uint256"
                    },
                    {
                        "name": "sqrtPriceLimitX96",
                        "type": "uint160",
                        "internalType": "uint160"
                    }
                ],
                "internalType": "struct IV3SwapRouter.ExactInputSingleParams"
            }
        ],
        "outputs": [
            {
                "name": "amountOut",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "exactOutput",
        "type": "function",
        "inputs": [
            {
                "name": "params",
                "type": "tuple",
                "components": [
                    {
                        "name": "path",
                        "type": "bytes",
                        "internalType": "bytes"
                    },
                    {
                        "name": "recipient",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "amountOut",
                        "type": "uint256",
                        "internalType": "uint256"
                    },
                    {
                        "name": "amountInMaximum",
                        "type": "uint256",
                        "internalType": "uint256"
                    }
                ],
                "internalType": "struct IV3SwapRouter.ExactOutputParams"
            }
        ],
        "outputs": [
            {
                "name": "amountIn",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "exactOutputSingle",
        "type": "function",
        "inputs": [
            {
                "name": "params",
                "type": "tuple",
                "components": [
                    {
                        "name": "tokenIn",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "tokenOut",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "fee",
                        "type": "uint24",
                        "internalType": "uint24"
                    },
                    {
                        "name": "recipient",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "amountOut",
                        "type": "uint256",
                        "internalType": "uint256"
                    },
                    {
                        "name": "amountInMaximum",
                        "type": "uint256",
                        "internalType": "uint256"
                    },
                    {
                        "name": "sqrtPriceLimitX96",
                        "type": "uint160",
                        "internalType": "uint160"
                    }
                ],
                "internalType": "struct IV3SwapRouter.ExactOutputSingleParams"
            }
        ],
        "outputs": [
            {
                "name": "amountIn",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "factory",
        "type": "function",
        "inputs": [],
        "outputs": [
            {
                "name": "",
                "type": "address",
                "internalType": "address"
            }
        ],
        "stateMutability": "view"
    },
    {
        "name": "factoryV2",
        "type": "function",
        "inputs": [],
        "outputs": [
            {
                "name": "",
                "type": "address",
                "internalType": "address"
            }
        ],
        "stateMutability": "view"
    },
    {
        "name": "getApprovalType",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "amount",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [
            {
                "name": "",
                "type": "uint8",
                "internalType": "enum IApproveAndCall.ApprovalType"
            }
        ],
        "stateMutability": "nonpayable"
    },
    {
        "name": "increaseLiquidity",
        "type": "function",
        "inputs": [
            {
                "name": "params",
                "type": "tuple",
                "components": [
                    {
                        "name": "token0",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "token1",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "tokenId",
                        "type": "uint256",
                        "internalType": "uint256"
                    },
                    {
                        "name": "amount0Min",
                        "type": "uint256",
                        "internalType": "uint256"
                    },
                    {
                        "name": "amount1Min",
                        "type": "uint256",
                        "internalType": "uint256"
                    }
                ],
                "internalType": "struct IApproveAndCall.IncreaseLiquidityParams"
            }
        ],
        "outputs": [
            {
                "name": "result",
                "type": "bytes",
                "internalType": "bytes"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "mint",
        "type": "function",
        "inputs": [
            {
                "name": "params",
                "type": "tuple",
                "components": [
                    {
                        "name": "token0",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "token1",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "fee",
                        "type": "uint24",
                        "internalType": "uint24"
                    },
                    {
                        "name": "tickLower",
                        "type": "int24",
                        "internalType": "int24"
                    },
                    {
                        "name": "tickUpper",
                        "type": "int24",
                        "internalType": "int24"
                    },
                    {
                        "name": "amount0Min",
                        "type": "uint256",
                        "internalType": "uint256"
                    },
                    {
                        "name": "amount1Min",
                        "type": "uint256",
                        "internalType": "uint256"
                    },
                    {
                        "name": "recipient",
                        "type": "address",
                        "internalType": "address"
                    }
                ],
                "internalType": "struct IApproveAndCall.MintParams"
            }
        ],
        "outputs": [
            {
                "name": "result",
                "type": "bytes",
                "internalType": "bytes"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "multicall",
        "type": "function",
        "inputs": [
            {
                "name": "previousBlockhash",
                "type": "bytes32",
                "internalType": "bytes32"
            },
            {
                "name": "data",
                "type": "bytes[]",
                "internalType": "bytes[]"
            }
        ],
        "outputs": [
            {
                "name": "",
                "type": "bytes[]",
                "internalType": "bytes[]"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "multicall",
        "type": "function",
        "inputs": [
            {
                "name": "deadline",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "data",
                "type": "bytes[]",
                "internalType": "bytes[]"
            }
        ],
        "outputs": [
            {
                "name": "",
                "type": "bytes[]",
                "internalType": "bytes[]"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "multicall",
        "type": "function",
        "inputs": [
            {
                "name": "data",
                "type": "bytes[]",
                "internalType": "bytes[]"
            }
        ],
        "outputs": [
            {
                "name": "results",
                "type": "bytes[]",
                "internalType": "bytes[]"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "positionManager",
        "type": "function",
        "inputs": [],
        "outputs": [
            {
                "name": "",
                "type": "address",
                "internalType": "address"
            }
        ],
        "stateMutability": "view"
    },
    {
        "name": "pull",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "value",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "refundETH",
        "type": "function",
        "inputs": [],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "selfPermit",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "value",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "deadline",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "v",
                "type": "uint8",
                "internalType": "uint8"
            },
            {
                "name": "r",
                "type": "bytes32",
                "internalType": "bytes32"
            },
            {
                "name": "s",
                "type": "bytes32",
                "internalType": "bytes32"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "selfPermitAllowed",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "nonce",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "expiry",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "v",
                "type": "uint8",
                "internalType": "uint8"
            },
            {
                "name": "r",
                "type": "bytes32",
                "internalType": "bytes32"
            },
            {
                "name": "s",
                "type": "bytes32",
                "internalType": "bytes32"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "selfPermitAllowedIfNecessary",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "nonce",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "expiry",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "v",
                "type": "uint8",
                "internalType": "uint8"
            },
            {
                "name": "r",
                "type": "bytes32",
                "internalType": "bytes32"
            },
            {
                "name": "s",
                "type": "bytes32",
                "internalType": "bytes32"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "selfPermitIfNecessary",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "value",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "deadline",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "v",
                "type": "uint8",
                "internalType": "uint8"
            },
            {
                "name": "r",
                "type": "bytes32",
                "internalType": "bytes32"
            },
            {
                "name": "s",
                "type": "bytes32",
                "internalType": "bytes32"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "swapExactTokensForTokens",
        "type": "function",
        "inputs": [
            {
                "name": "amountIn",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "amountOutMin",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "path",
                "type": "address[]",
                "internalType": "address[]"
            },
            {
                "name": "to",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [
            {
                "name": "amountOut",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "swapTokensForExactTokens",
        "type": "function",
        "inputs": [
            {
                "name": "amountOut",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "amountInMax",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "path",
                "type": "address[]",
                "internalType": "address[]"
            },
            {
                "name": "to",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [
            {
                "name": "amountIn",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "payable"
    },
    {
        "name": "sweepToken",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "amountMinimum",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "recipient",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "sweepToken",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "amountMinimum",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "sweepTokenWithFee",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "amountMinimum",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "feeBips",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "feeRecipient",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "sweepTokenWithFee",
        "type": "function",
        "inputs": [
            {
                "name": "token",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "amountMinimum",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "recipient",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "feeBips",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "feeRecipient",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "uniswapV3SwapCallback",
        "type": "function",
        "inputs": [
            {
                "name": "amount0Delta",
                "type": "int256",
                "internalType": "int256"
            },
            {
                "name": "amount1Delta",
                "type": "int256",
                "internalType": "int256"
            },
            {
                "name": "_data",
                "type": "bytes",
                "internalType": "bytes"
            }
        ],
        "outputs": [],
        "stateMutability": "nonpayable"
    },
    {
        "name": "unwrapWETH9",
        "type": "function",
        "inputs": [
            {
                "name": "amountMinimum",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "recipient",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "unwrapWETH9",
        "type": "function",
        "inputs": [
            {
                "name": "amountMinimum",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "unwrapWETH9WithFee",
        "type": "function",
        "inputs": [
            {
                "name": "amountMinimum",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "recipient",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "feeBips",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "feeRecipient",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "unwrapWETH9WithFee",
        "type": "function",
        "inputs": [
            {
                "name": "amountMinimum",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "feeBips",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "feeRecipient",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "name": "wrapETH",
        "type": "function",
        "inputs": [
            {
                "name": "value",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [],
        "stateMutability": "payable"
    },
    {
        "type": "receive",
        "stateMutability": "payable"
    }
]