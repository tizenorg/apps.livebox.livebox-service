/*
 * Copyright 2013  Samsung Electronics Co., Ltd
 *
 * Licensed under the Flora License, Version 1.1 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://floralicense.org/license/
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

extern double util_timestamp(void);
extern const char *util_basename(const char *name);
extern unsigned long util_free_space(const char *path);
extern char *util_replace_string(const char *src, const char *pattern, const char *replace);
extern const char *util_uri_to_path(const char *uri);
extern int util_validate_livebox_package(const char *pkgname);
extern char *util_conf_get_libexec(const char *pkgname);
extern char *util_id_to_uri(const char *id);	/* For FILENAME id */

#define SCHEMA_FILE	"file://"
#define SCHEMA_PIXMAP	"pixmap://"
#define SCHEMA_SHM	"shm://"

/* End of a file */
