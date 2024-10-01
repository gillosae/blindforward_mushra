import pandas as pd

df = pd.read_csv("mushra_temp.csv")

split_data = {exp_type: df_group for exp_type, df_group in df.groupby("exp")}
# print(split_data)


# afx_learning_single


# ref_dry /ssd4/doyo/test_set_v2/single_effects_rand_param/vctk1/aac/aac-hard-1-dry_ref.wav
# ref_wet /ssd4/doyo/test_set_v2/single_effects_rand_param/vctk1/aac/aac-hard-1-wet_ref.wav,
# tar_dry /ssd4/doyo/test_set_v2/single_effects_rand_param/vctk1/aac/aac-hard-1-dry_tar.wav,
# tar_wet /ssd4/doyo/test_set_v2/single_effects_rand_param/vctk1/aac/aac-hard-1-wet_tar.wav,
# pred1 /ssd4/doyo/infer_forward_final/train_single-eval_single/vctk1/aac_hard-1-2wet_tar.wav,
# pred2 /ssd4/doyo/infer_forward_final/train_multi-eval_single/vctk1/aac_hard-1-2wet_tar.wav,
# random_param /ssd4/doyo/test_set_v2/single_effects_rand_param_2/vctk1/aac/aac-moderate-1-wet_tar.wav
afx_learning_single = split_data["afx_learning_single"]


afx_learning_single["ref_dry"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/single_effects_rand_param/vctk1/{row['subtype']}/{row['subtype']}-hard-{row['num']}-dry_ref.wav",
    axis=1,
)
afx_learning_single["ref_wet"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/single_effects_rand_param/vctk1/{row['subtype']}/{row['subtype']}-hard-{row['num']}-wet_ref.wav",
    axis=1,
)
afx_learning_single["tar_dry"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/single_effects_rand_param/vctk1/{row['subtype']}/{row['subtype']}-hard-{row['num']}-dry_tar.wav",
    axis=1,
)
afx_learning_single["tar_wet"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/single_effects_rand_param/vctk1/{row['subtype']}/{row['subtype']}-hard-{row['num']}-wet_tar.wav",
    axis=1,
)
afx_learning_single["pred1"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/infer_forward_final/train_single-eval_single/vctk1/{row['subtype']}_hard-{row['num']}-2wet_tar.wav",
    axis=1,
)
afx_learning_single["pred2"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/infer_forward_final/train_multi-eval_single/vctk1/{row['subtype']}_hard-{row['num']}-2wet_tar.wav",
    axis=1,
)
afx_learning_single["random_param"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/single_effects_rand_param_2/vctk1/{row['subtype']}/{row['subtype']}-moderate-{row['num']}-wet_tar.wav",
    axis=1,
)
print(afx_learning_single)


# afx_learning_multi

# ref_dry /ssd4/doyo/test_set_v2/multi_effects/vctk1/complex_0/complex_0-_-0-dry_ref.wav,
# ref_wet /ssd4/doyo/test_set_v2/multi_effects/vctk1/complex_0/complex_0-_-0-wet_ref.wav,
# tar_dry /ssd4/doyo/test_set_v2/multi_effects/vctk1/complex_0/complex_0-_-0-dry_tar.wav,
# tar_wet /ssd4/doyo/test_set_v2/multi_effects/vctk1/complex_0/complex_0-_-0-wet_tar.wav,
# pred1 /ssd4/doyo/infer_forward_final/train_single-eval_multi/vctk1/complex_0-0-3pred.wav,
# pred2 /ssd4/doyo/infer_forward_final/train_multi-eval_multi/vctk1/complex_0-0-3pred.wav,
# random_param -

afx_learning_multi = split_data["afx_learning_multi"]

afx_learning_single["ref_dry"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/multi_effects/vctk1/{row['subtype']}/{row['subtype']}-_-{row['num']}-dry_ref.wav",
    axis=1,
)
afx_learning_single["ref_wet"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/multi_effects/vctk1/{row['subtype']}/{row['subtype']}-_-{row['num']}-wet_ref.wav",
    axis=1,
)
afx_learning_single["tar_dry"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/multi_effects/vctk1/{row['subtype']}/{row['subtype']}-_-{row['num']}-dry_tar.wav",
    axis=1,
)
afx_learning_single["tar_wet"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/multi_effects/vctk1/{row['subtype']}/{row['subtype']}-_-{row['num']}-wet_tar.wav",
    axis=1,
)
afx_learning_single["pred1"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/infer_forward_final/train_single-eval_multi/vctk1/{row['subtype']}-{row['num']}-3pred.wav",
    axis=1,
)
afx_learning_single["pred2"] = afx_learning_single.apply(
    lambda row: f"/ssd4/doyo/infer_forward_final/train_multi-eval_multi/vctk1/{row['subtype']}-{row['num']}-3pred.wav",
    axis=1,
)
print(afx_learning_multi)


# recording_env

# ref_dry /ssd4/doyo/test_set_v2/single_effects_multi_env/vctk1/libopus/libopus-hard-2-dry_ref.wav,
# ref_wet /ssd4/doyo/test_set_v2/single_effects_multi_env/vctk1/libopus/libopus-hard-2-wet_ref.wav,
# tar_dry /ssd4/doyo/test_set_v2/single_effects_multi_env/vctk1/libopus/libopus-hard-2-dry_tar.wav,
# tar_wet /ssd4/doyo/test_set_v2/single_effects_multi_env/vctk1/libopus/libopus-hard-2-wet_tar.wav,
# pred1 /ssd4/doyo/infer_forward_exp2-rec_env/single_recording_env/vctk1/libopus_hard-2-3pred.wav,
# pred2 /ssd4/doyo/infer_forward_exp2-rec_env/multiple_recording_env/vctk1/libopus_hard-2-3pred.wav,
# random_param /ssd4/doyo/test_set_v2/single_effects_multi_rand_param/vctk1/libopus/libopus-hard-2-wet_tar.wav
recording_env = split_data["recording_env"]

recording_env["ref_dry"] = recording_env.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/single_effects_multi_env/vctk1/{row['subtype']}/{row['subtype']}-hard-{row['num']}-dry_ref.wav",
    axis=1,
)
recording_env["ref_wet"] = recording_env.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/single_effects_multi_env/vctk1/{row['subtype']}/{row['subtype']}-hard-{row['num']}-wet_ref.wav",
    axis=1,
)
recording_env["tar_dry"] = recording_env.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/single_effects_multi_env/vctk1/{row['subtype']}/{row['subtype']}-hard-{row['num']}-dry_tar.wav",
    axis=1,
)
recording_env["tar_wet"] = recording_env.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/single_effects_multi_env/vctk1/{row['subtype']}/{row['subtype']}-hard-{row['num']}-wet_tar.wav",
    axis=1,
)
recording_env["pred1"] = recording_env.apply(
    lambda row: f"/ssd4/doyo/infer_forward_exp2-rec_env/single_recording_env/vctk1/{row['subtype']}_hard-{row['num']}-3pred.wav",
    axis=1,
)
recording_env["pred2"] = recording_env.apply(
    lambda row: f"/ssd4/doyo/infer_forward_exp2-rec_env/multiple_recording_env/vctk1/{row['subtype']}_hard-{row['num']}-3pred.wav",
    axis=1,
)
recording_env["random_param"] = recording_env.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/single_effects_rand_param_2/vctk1/{row['subtype']}/{row['subtype']}-moderate-{row['num']}-wet_tar.wav",
    axis=1,
)
print(recording_env)


# cross_domain

# ref_dry /ssd4/doyo/test_set_v2/cross_domain_single/maestro_single/aac/aac-hard-33-dry_ref.wav,
# ref_wet /ssd4/doyo/test_set_v2/cross_domain_single/maestro_single/aac/aac-hard-33-wet_ref.wav,
# tar_dry /ssd4/doyo/test_set_v2/cross_domain_single/maestro_single/aac/aac-hard-3-dry_tar.wav,
# tar_wet /ssd4/doyo/test_set_v2/cross_domain_single/maestro_single/aac/aac-hard-3-wet_tar.wav,
# pred1 /ssd4/doyo/infer_forward_cross_domain/cross_domain/maestro_single/aac_hard-33-3pred.wav,
# pred2 -,
# random_param /ssd4/doyo/test_set_v2/cross_domain_single_rand_param/maestro_single/aac/aac-hard-33-wet_tar.wav

cross_domain = split_data["cross_domain"]

cross_domain["ref_dry"] = cross_domain.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/cross_domain_single/maestro_single/{row['subtype']}/{row['subtype']}-hard-{row['num']}-dry_ref.wav",
    axis=1,
)
cross_domain["ref_wet"] = cross_domain.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/cross_domain_single/maestro_single/{row['subtype']}/{row['subtype']}-hard-{row['num']}-wet_ref.wav",
    axis=1,
)
cross_domain["tar_dry"] = cross_domain.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/cross_domain_single/maestro_single/{row['subtype']}/{row['subtype']}-hard-{row['num']}-dry_tar.wav",
    axis=1,
)
cross_domain["tar_wet"] = cross_domain.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/cross_domain_single/maestro_single/{row['subtype']}/{row['subtype']}-hard-{row['num']}-wet_tar.wav",
    axis=1,
)
cross_domain["pred1"] = cross_domain.apply(
    lambda row: f"/ssd4/doyo/infer_forward_cross_domain/cross_domain/maestro_single/{row['subtype']}_hard-{row['num']}-3pred.wav",
    axis=1,
)
cross_domain["random_param"] = cross_domain.apply(
    lambda row: f"/ssd4/doyo/test_set_v2/cross_domain_single_rand_param/maestro_single/{row['subtype']}/{row['subtype']}-moderate-{row['num']}-wet_tar.wav",
    axis=1,
)
print(cross_domain)
