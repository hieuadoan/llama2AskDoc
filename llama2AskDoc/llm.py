from langchain.llms import CTransformers

# Local CTransformers wrapper for Llama-2-7B-Chat
llm = CTransformers(model='/lcrc/project/QM_Storage/meta_llama/llama.cpp/models/7B-chat/ggml-model-7bchat-q8_0.bin', # Location of downloaded GGML model
                    model_type='llama', # Model type Llama
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})
