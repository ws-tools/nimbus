/*
 * Copyright 1999-2008 University of Chicago
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy
 * of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */

package org.nimbustools.api._repr.ctx;

import org.nimbustools.api.repr.ctx.Context;

/**
 * This is currently just what the Manager needs to consume.
 *
 * Virtualization of ContextBroker itself is coming in subsequent release.
 */
public interface _Context extends Context {

    public void setBootstrapText(String bootstrapText);
    public void setBootstrapPath(String bootstrapPath);
}
